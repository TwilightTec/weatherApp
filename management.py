import tkinter as tk
from tkinter import messagebox
class management:
    def __init__(self, master, weatherApp):
        self.master = master
        self.weatherApp = weatherApp
        #setting the windiow to incurr the same properties as the main window
        self.window = tk.Toplevel(self.master)
        self.window.title("Management")
        self.window.geometry("400x400")
        #creating the labels for the credentials
        self.usernameLabel = tk.Label(self.window, text = "Username: ")
        self.usernameLabel.pack(pady = 5)
        self.usernameEntry = tk.Entry(self.window)
        self.usernameEntry.pack(pady = 5)
        self.passwordLabel = tk.Label(self.window, text = "Password: ")
        self.passwordEntry = tk.Entry(self.window, show = "*")
        self.passwordEntry.pack(pady = 5)
        self.loginButton = tk.Button(self.window, text = "Login", command = self.login)
        self.loginButton.pack(pady = 10)
    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username == "admin" and password == "1234":
            self.showApiKey()
        else:
            messagebox.showeroor("Incorrect")
    def showApiKey(self):
        self.apiKeyLabel = tk.Label(self.window, text = f"Current API Key: {self.weatherApp.apiKey}")
        self.apiKeyLabel.pack(pady = 10)
        self.newApiLabel = tk.Label(self.window, text = "Enter the new API key: ")
        self.newApiLabel.pack(pady = 5)
        self.apiKeyEntry = tk.Entry(self.window)
        self.apiKeyEntry.pack(pady = 5)
        self.submitButton = tk.Button(self.window, text = "Submit", command = self.updateApiKey)
        self.submitButton.pack(pady = 10)
##logic for updating the the API key if needed 
    def updateApiKey(self):
        newApiKey = self.apiKeyEntry.get().strip()
        if newApiKey:
            self.weatherApp.updateApiKey(newApiKey)
            messagebox.showinfo("Success")
            self.window.destroy()
        else:
            messagebox.showinfo("Error")
