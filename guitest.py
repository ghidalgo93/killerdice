# Import Libraries
import tkinter

# Dice class, rolls will be decided at the moment of dice instantiation

# Dice list = []

# Actual GUI
top = tkinter.Tk()
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

top.mainloop()



