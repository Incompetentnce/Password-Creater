#imports
import random 
import time
from pathlib import Path
import string
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import pyperclip
window = tk.Tk()

#Setup creating the password

lengthOfPassword = random.randint(7,14)

def storeInFile(strength):
    strength = strength
    finalPassword = createCombinedPassword(strength)
    print(f"Your password is {finalPassword}")

    if strength == 8:
        strength = "Weak"
    elif strength == 12:
        strength = "Strong"
    elif strength == 16:
        strength = "SuperStrong"

    with open("password.txt", "a+") as f:
        f.write(f"{finalPassword} Strength: {strength}\n")

    passwordLabel.config(text=f"{finalPassword}")  # Update the label text
    return finalPassword

def copyPassword():
    password = passwordLabel.cget("text")
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied", "The password has been copied to the clipboard.")
        
    
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
    
def createLabel(text):
    label = tk.Label(window, text=text, font=("Courier New",16))
    label.grid(row=0, column=0, columnspan=3, padx=50, pady=100, sticky="nsew")
  
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


window.title("Password Generator")

# Create labels



# Create buttons
weakButton = tk.Button(window, text="Weak", width=50, height=10, font=("Courier New",16), bg="#3d3dff", fg="white", highlightbackground="#3d3dff")
strongButton = tk.Button(window, text="Strong", width=50, height=10, font=("Courier New",16), bg="#3d3dff", fg="white", highlightbackground="#3d3dff")
superStrongButton = tk.Button(window, text="Super Strong", width=50, height=10, font=("Courier New",16), bg="#3d3dff", fg="white", highlightbackground="#3d3dff")

# Grid layout for labels

weakaction = actionsButtonWeak
strongaction = actionsButtonStrong
superStrongaction = actionsButtonSuperStrong

passwordLabel = tk.Label(window, text="", font=("Courier New", 16), fg="black")
passwordLabel.grid(row=0, column=0, columnspan=3, padx=50, pady=100, sticky="nsew")

# Grid layout for buttons
weakButton.grid(row=1, column=0, padx=50, pady=100, sticky="nsew")
strongButton.grid(row=1, column=1, padx=50, pady=100, sticky="nsew")
superStrongButton.grid(row=1, column=2, padx=50, pady=100, sticky="nsew")
copyButton = ttk.Button(window, text="Copy", command=copyPassword)
copyButton.grid(row=2, column=0, columnspan=3, padx=50, pady=10, sticky="nsew")

# Configure grid columns to expand and center the buttons
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

#bind the buttons
weakButton.bind("<Button-1>", weakaction)
strongButton.bind("<Button-1>", strongaction)
superStrongButton.bind("<Button-1>", superStrongaction)



# Configure grid row to expand
window.grid_rowconfigure(1, weight=1)

# Start the main event loop
window.mainloop()
