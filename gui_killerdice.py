# Gerardo Hidalgo-Cuellar
# KillerDice, a dice rolling tkinter application that will roll dice for you
# 8/5/2020 https://github.com/ghidalgo93

# Import Libraries
import tkinter as tk
import random


# dice list that will be populated as dice are added
dice_list = []

# Functions
def roll(dice_kind):
    dice_list.append(random.randint(1,dice_kind))
    lbl_tray["text"] = dice_list

def roll_total():
    dice_total = 0
    for d in dice_list:
        dice_total = dice_total + d
    lbl_total["text"] = dice_total

# Create Window and Title 
window = tk.Tk()
window.title("Killer Dice")


# Configure Rows and Collumns
window.columnconfigure([0,1,2,3,4,5], minsize=50,  weight=1)
window.rowconfigure([0,1,2,3], minsize=50)

# Roll buttons
btn_d4 = tk.Button(master=window, text="D4", width=10, height=5, command=roll(4))
btn_d4.grid(row=0, column=0, sticky="nsew")

btn_d6 = tk.Button(master=window, text="D6", width=10, height=5, command=roll(6))
btn_d6.grid(row=0, column=1, sticky="nsew")

btn_d8 = tk.Button(master=window, text="D8", width=10, height=5, command=roll(8))
btn_d8.grid(row=0, column=2, sticky="nsew")

btn_d10 = tk.Button(master=window, text="D10", width=10, height=5, command=roll(10))
btn_d10.grid(row=0, column=3, sticky="nsew")

btn_d12 = tk.Button(master=window, text="D12", width=10, height=5, command=roll(12))
btn_d12.grid(row=0, column=4, sticky="nsew")

btn_d20 = tk.Button(master=window, text="D20", width=10, height=5, command=roll(20))
btn_d20.grid(row=0, column=5, sticky="nsew")

# Modifier Loader
#TODO
# lbl_modifier = tk.Label(master=window, text="NONE")
#lbl_modifier.grid(row=1, column=3)

# Dice Tray
lbl_tray = tk.Label(master=window, text="0", height=15)
lbl_tray.grid(row=2, column=3)

# Roll Button
btn_roll = tk.Button(master=window, text="Roll", width=10, height=5, command=roll_total)
btn_roll.grid(row=3, column=0, sticky="nsew")

# Total
lbl_total = tk.Label(master=window, text="Total: ")
lbl_total.grid(row=3, column=5)


# Dice class, rolls will be decided at the moment of dice instantiation
# Dice list = []

# Actual GUI
# Top horizontal slider with radio buttons (different dice selectors), images above each radio button
    #logic: on button press, the pane below will show up with the selected dice +/- modifier addition
    #once the submit button is pressed on the mod-pane, deselect radio button

# When a radio button is pressed, a pane shows up below and allows for modifiers, has some kind of 'submit' button to push to the dice tray
    #logic: doesn't show up until radio button pressed, and once 'submit' is pressec it...
    #1) instantiates a die with that modifier and adds it to the dicelist
    #2) deselects the radio button in the h-slider


#dice tray, some kind of visual representation of the dice you have put in thus far with a 'roll' button somewhere
    #logic: when 'roll' button is pressed, it will add all of the modified rolls in the dice list together
    #eventually some kind of annimation
    #give you the roll of all the dice







window.mainloop()



