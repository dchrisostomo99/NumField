"""
Program: numField.py
Author: Daniel Chrisostomo
"""
from breezypythongui import *
import math 

class NumberFieldDemo(EasyFrame):
    """"Computes and displays square root of an input number."""
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title= "Number Field Demo")
        #Label and field for the input  
        self.first = self.addLabel(text = "Enter a number", row = 0, column = 0, background = "red", foreground = "blue")
        self.inputField = self.addIntegerField(value = "", row = 0, column = 1, width = 10)
        #Label and field for the second input
        self.second = self.addLabel(text = "Enter another number", row = 1, column = 0)
        self.inputField2 = self.addIntegerField(value = "", row = 1, column = 1, width = 10)
        
        #Label and field for the output 
        self.third = self.addLabel(text = "Add", row = 2, column = 0)
        self.outputField1 = self.addFloatField(value = "", row = 2, column = 1, width = 8, precision = 2, state = "readonly")

        self.four = self.addLabel(text = "Sub", row = 3, column = 0)
        self.outputField2 = self.addFloatField(value = "", row = 3, column = 1, width = 8, precision = 2, state = "readonly")

        self.five = self.addLabel(text = "Multiply", row = 4, column = 0)
        self.outputField3 = self.addFloatField(value = "", row = 4, column = 1, width = 8, precision = 2, state = "readonly")

        self.third = self.addLabel(text = "Divide", row = 5, column = 0)
        self.outputField4 = self.addFloatField(value = "",  row = 5, column = 1, width = 8, precision = 2, state = "readonly")
        
        #The command button  
        self.Btn = self.addButton(text = "Compute", row = 6, column = 2, columnspan = 2, command = self.computeSub)
        self.Btn["background"] = "red"
        self.Btn["foreground"] = "blue"
        # The event handling method for the button  

    def computeSub(self):
        """Inputs the integer, computes the difference """
        try:
            number = self.inputField.getNumber()
            number2 = self.inputField2.getNumber()
            result = number + number2
            self.outputField1.setNumber(result)

            number = self.inputField.getNumber()
            number2 = self.inputField2.getNumber()
            result = number - number2
            self.outputField2.setNumber(result)

            number = self.inputField.getNumber()
            number2 = self.inputField2.getNumber()
            result = number * number2
            self.outputField3.setNumber(result)

            number = self.inputField.getNumber()
            number2 = self.inputField2.getNumber()
            result = number / number2
            self.outputField4.setNumber(result)
        except ValueError:
            self.messageBox(title = "ERROR", message = "Input must be an integer >= O")            
                   
def main():
    NumberFieldDemo().mainloop()
main()    
