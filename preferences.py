import tkinter as tk
import requests
class preferences:
    def __init__(self,master, weatherApp):
        #refers to keeping the size and attributues of the main window
        self.master = master
        self.weatherApp = weatherApp
        #creates a new independent window
        self.window = tk.Toplevel(self.master)
        self.window.title("Preferences")
        self.window.geometry("500x500")
        #setting the default value for the three preferences options
        self.temperatureUnit = tk.StringVar(value = "F")
        self.weatherNotifications = tk.BooleanVar(value = True)
        self.backgroundColor = tk.StringVar(value = self.weatherApp.backgroundColor)
        self.updateBackground()
        #creating and packing the labels and buttons for each of the preferences option for the GUI
        self.temperatureLabel = tk.Label(self.window, text = "Temperature Unit: ")
        self.temperatureLabel.pack(anchor = "center", padx = 20, pady =10)
        self.temperatureFahrenheit = tk.Radiobutton(self.window, text = "Fahrenheit", variable = self.temperatureUnit, value = "F")
        self.temperatureFahrenheit.pack(anchor = "center", padx = 40, pady =5)
        self.temperatureCelsius = tk.Radiobutton(self.window, text = "Celsius" , variable = self.temperatureUnit, value = "C")
        self.temperatureCelsius.pack(anchor = "center", padx = 40, pady = 5)
        self.weatherLabel= tk.Label(self.window , text = "Severe Weather Notifications: ")
        self.weatherLabel.pack(anchor = "center", padx=20, pady= 10)
        self.weatherOn = tk.Radiobutton(self.window, text = "On", variable = self.weatherNotifications, value = True)
        self.weatherOn.pack(anchor = "center", padx = 40, pady =5)
        self.weatherOff = tk.Radiobutton(self.window, text = "Off", variable = self.weatherNotifications, value = False)
        self.weatherOff.pack(anchor = "center",  padx = 40, pady = 5)
        self.backgroundLabel = tk.Label(self.window, text = "Background Color: ")
        self.backgroundLabel.pack(anchor = "center", padx = 20, pady = 10)
        self.backgroundDefault = tk.Radiobutton(self.window, text = "Default", variable = self.backgroundColor, value = "Default", command = self.updateBackground)
        self.backgroundDefault.pack(anchor = "center", padx= 40, pady = 5)
        self.backgroundWhite = tk.Radiobutton(self.window, text = "White", variable = self.backgroundColor, value = "White", command = self.updateBackground)
        self.backgroundWhite.pack(anchor = "center", padx = 40, pady = 5)
        #submit button at the bottom of the window
        submit = tk.Button(self.window, text = "Submit", command = self.onSubmit)
        submit.pack(pady= 10)
    #code that runs when the submit buttoon is clicked
    def onSubmit(self):
        #setting the updated values to their appropiate variables
        temperatureUnit = self.temperatureUnit.get()
        weatherNotifications = self.weatherNotifications.get()
        backgroundColor = self.backgroundColor.get()
        self.weatherApp.updatePreferences(temperatureUnit, weatherNotifications, backgroundColor)
        #closing the preferences window when done
        self.window.destroy()
        #code that updates the background when needed
    def updateBackground(self):
        selectedColor = self.backgroundColor.get()
        if selectedColor == "White":
            self.weatherApp.window.config(bg = "white")
        elif selectedColor == "Default":
            self.weatherApp.window.config(bg = "SystemButtonFace")
            self.weatherApp.backgroundLabel.place(relwidth = 1, relheight = 1)
                
            
