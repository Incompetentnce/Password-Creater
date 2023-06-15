#imports
import random 
import time
from pathlib import Path
import string
import tkinter as tk


#Setup creating the password

lengthOfPassword = random.randint(7,14)

def createPasswordLowercase(length):
    characters = string.ascii_lowercase
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
        
def createPasswordUppercase(length):
    characters = string.ascii_uppercase
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def createPasswordOther(length):
    characters = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', '~', '`', '|', '/', '?', '.']
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def createCombinedPassword(length):
    lowercaseLength = length // 2
    uppercaseLength = length // 4
    otherLength = length // 4
    lowercasePassword = createPasswordLowercase(lowercaseLength)
    uppercasePassword = createPasswordUppercase(uppercaseLength)
    otherPassword = createPasswordOther(otherLength)
    combinedPassword = lowercasePassword + uppercasePassword + otherPassword
    combined_password = list(combinedPassword)
    random.shuffle(combined_password)
    combinedPassword = ''.join(combined_password)
    return combinedPassword
    
    
#determining how secure

weak = 8
strong = 12
superStrong = 16
#strength = input("How strong would you like your password to be? (weak, strong, super strong) ")
strength = "ak"
if strength == "weak":
    strength = weak
if strength == "strong":
    strength = strong
if strength == "super strong":
    strength = superStrong
#misc needed variables
#combined_password = createCombinedPassword(strength)
#print(combined_password)

window = tk.Tk()
window.title("Password Generator")

weakLabel = tk.Label(window, text = "Weak")
StrongLabel = tk.Label(window, text = "Strong")
superStrongLabel = tk.Label(window, text = "Super Strong")
strengthOptions = [weak, strong, superStrong]
weakButton = tk.Button(window, text="Weak")
strongButton = tk.Button(window, text="Strong")
superStrongButton = tk.Button(window, text="Super Strong")
window.grid_columnconfigure(0, weight = 1, uniform="buttons")
window.grid_columnconfigure(1, weight = 1, uniform="buttons")
window.grid_columnconfigure(2, weight = 1, uniform="buttons")
weakButton.grid(row = 0, column = 0)
strongButton.grid(row = 0, column = 1)
superStrongButton.grid(row = 0, column = 2)

window.mainloop()
