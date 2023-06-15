#imports
import random 
import time
from pathlib import Path
import string
import tkinter as tk


#Setup creating the password

lengthOfPassword = random.randint(7,14)

def storeInFile(strength):
    strength = strength
    finalPassword = createCombinedPassword(strength)
    print(f"Your password is {finalPassword}")
    
    
    
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

def actionsButtonWeak(event):
    #print("weak")
    strength = 8
    storeInFile(strength)
    
    
def actionsButtonStrong(event):
    #print("strong")
    strength = 12
    storeInFile(strength)
    
def actionsButtonSuperStrong(event):
    #print("super strong")
    strength = 16
    storeInFile(strength)
    
    
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


# Create buttons
weakButton = tk.Button(window, text="Weak", width=50, height=10, font=("Courier New",16), bg="#3d3dff", fg="white", highlightbackground="#3d3dff")
strongButton = tk.Button(window, text="Strong", width=50, height=10, font=("Courier New",16), bg="#3d3dff", fg="white", highlightbackground="#3d3dff")
superStrongButton = tk.Button(window, text="Super Strong", width=50, height=10, font=("Courier New",16), bg="#3d3dff", fg="white", highlightbackground="#3d3dff")

# Grid layout for labels


# Grid layout for buttons
weakButton.grid(row=1, column=0, padx=50, pady=100, sticky="nsew")
strongButton.grid(row=1, column=1, padx=50, pady=100, sticky="nsew")
superStrongButton.grid(row=1, column=2, padx=50, pady=100, sticky="nsew")

# Configure grid columns to expand and center the buttons
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

#bind the buttons
weakButton.bind("<Button-1>", actionsButtonWeak)
strongButton.bind("<Button-1>", actionsButtonStrong)
superStrongButton.bind("<Button-1>", actionsButtonSuperStrong)


# Configure grid row to expand
window.grid_rowconfigure(1, weight=1)

# Start the main event loop
window.mainloop()
