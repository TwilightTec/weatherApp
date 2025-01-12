#importing tkinter for the graphical functions
import tkinter as tk
from preferences import preferences
from management import management
import requests
class weatherApp:
    def __init__(self):
        #setting up the current window and it's properties
        self.window = tk.Tk()
        self.window.title("Weather App")
        self.window.geometry("500x500")
        self.temperatureUnit = "F"
        #setting the default values for labels
        self.weatherNotifications = True
        self.backgroundColor = "Default"
        self.backgroundImage = tk.PhotoImage(file ="weatherBackground.png")
        self.backgroundLabel = tk.Label(self.window, image =self. backgroundImage)
        self.notificationImage = tk.PhotoImage(file = "notification.png")
        self.managementImage = tk.PhotoImage(file = "management.png")
        self.notificationLabel = None
        self.displayNotificationImage()
        self.managementLabel = None
        self.displayManagementImage()
        #relwidth can be between 0 and 1
        self.backgroundLabel.place(relwidth = 1, relheight = 1)
        self.apiKey = "a81c7a9e93fb3340dde2399b26580475"
        self.cities = ["Paris", "Rome", "Lagos", "Tokyo", "New York"]
        #creating row and column values for displaying the citites
        columnValue = 0
        rowValue = 0
        #dictionaries to hold the buttons, labels, and city data
        self.cityButtons = {}
        self.cityLabels = {}
        self.cityData = {}
        #loop over each city to retrieve it's temperature
        for a in range (5):
            city = self.cities[a]
            details ={
                "q": city,
                "appid": self.apiKey,
                "units" : "imperial"
                }
            response = requests.get("http://api.openweathermap.org/data/2.5/weather",params = details)
            #a code of 200 incidcates a succesfull API call
            if response.status_code == 200:
                data = response.json()
                #this information is needed for the alerts used later in the code
                latitude =data ["coord"]["lat"]
                longitude =data ["coord"]["lon"]
                temperature = data["main"]["temp"]
                #converting the temperature into a whole number
                temperature = int(temperature)
                #formating the temperature for proper display
                label = tk.Label(self.window, text = f"{temperature} °F", font = ("Helvectica", 30), bg = "grey", fg= "black", bd = 3, relief = "sunken" )

                label.place(x=columnValue, y = rowValue)
                #setting the city label to the current city based of the current iteration
                self.cityLabels[city] = label
                #cities button images being uploaded
                cityButtonImage = tk.PhotoImage(file = f"{city.lower()}.png")
                self.cityButtons[city] = {'button':  tk.Button(self.window, image = cityButtonImage, relief = "flat"),
                                          'image': cityButtonImage}
                self.cityButtons[city] ['button'].place(x =columnValue, y = rowValue + 50)
                self.cityData[city] = {"temperature" : temperature, "alerts": None}
                #incrementing the row and column values by 100 each iteration
                columnValue += 100
                rowValue += 100
            #if severe weather alerts are turned on the following code will rrun   
            if "alerts" in data:
                alerts = data["alerts"]
                alertMessage = "\n".join([alert["description"] for alert in alerts])
                self.cityData[city]["alerts"] = alertMessage
            else:
                self.cityData[city]["alerts"] = None
        #creating the preferencesButton in the top right hand corne rof the screen
        preferencesButton = tk.Button(self.window,text = "Preferences", command = self.openPreferences)
        preferencesButton.place(x = 380, y = 10)
        self.window.mainloop()
        #a new window is created when the prefereneces button is clicked
    def openPreferences(self):
        preferences(self.window, self)
        #function to update the three different preferences options when needed
    def updatePreferences(self, temperatureUnit,weatherNotifications, backgroundColor):
        self.temperatureUnit = temperatureUnit
        self.weatherNotifications = weatherNotifications
        self.backgroundColor = backgroundColor
        if backgroundColor == "White":
            self.backgroundLabel.place_forget()
            self.window.config(bg = "white")
        elif backgroundColor == "Default":
            self.window.config(bg = "SystemButtonFace")
            self.backgroundLabel.place(relwidth = 1, relheight = 1)
        if weatherNotifications:
            self.displayNotificationImage()
        else:
            self.hideNotificationImage()
        self.updateTemperature()
    #function that shows the notifications label that hold severe weather information
    def displayNotificationImage(self):
        if self.notificationLabel is None:
            self.notificationLabel = tk.Label(self.window, image = self.notificationImage, bg = "grey")
            self.notificationLabel.place(x=0, y = 463)
            self.notificationLabel.bind("<Button-1>", self.showAlerts)
            #if the severe weather alerts are turned off this function will run
    def hideNotificationImage(self):
        if self.notificationLabel is not None:
            self.notificationLabel.place_forget()
            self.notificationLabel = None
            #function to show the severe weather alerts by using the the data retrieved from the API call
    def showAlerts(self,event):
        alertWindow = tk.Toplevel(self.window)
        alertWindow.geometry("500x500")
        alertText = tk.Text(alertWindow, wrap = tk.WORD, height = 10, width = 40)
        alertText.pack(pady = 10)
        #one line of alerts for each city
        for city, data in self.cityData.items():
            if data["alerts"]:
                alertText.insert(tk.END, f"Alerts for {city}: \n{data['alerts']}\n\n")
                #line that displays when there are no severe weather alerts for said city
            else:
                alertText.insert(tk.END, f"No alerts for {city}. \n\n")
                #this is a read only widget so the state is disabled
        alertText.config(state = tk.DISABLED)
        #if the user prefers to view the temperature in celsius then this function runs
    def updateTemperature(self):
        for city, data in self.cityData.items():
            #conversion rate for the temperature unit change
            if self.temperatureUnit == "C":
                temperature = (data["temperature"] - 32) * 5/9
                temperature = int(temperature)
                self.cityLabels[city].config(text = f"{temperature} °C")
            else:
                temperature = data["temperature"]
                self.cityLabels[city].config(text = f"{temperature}  °F")
                #management label configuration
    def displayManagementImage(self):
        if self.managementLabel is None:
            self.managementLabel = tk.Label(self.window, image = self.managementImage, bg = "grey")
            self.managementLabel.place(x = 10, y= 430)
            self.managementLabel.bind("<Button - 1>", self.openManagement)
            #opening the management window
    def openManagement(self, event):
        management(self.window, self)
        #this fucntion will run if updating the API is needed
    def updateApiKey(self, newApiKey):
        self.apiKey = newApiKey
weatherApp()
