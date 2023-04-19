# Test-Calculator

from tkinter import *

class Calculator:
    def __init__(self):
        window = Tk()
        window.title("Calculator")

        self.display = StringVar()
        display = Entry(window, textvariable = self.display, justify = RIGHT)
        display.grid(row = 1, column = 1, columnspan = 4, sticky = W + E)

        Button(window, text = "1", command = lambda: self.press("1")).grid(row = 2, column = 1, sticky = W + E)
        Button(window, text = "2", command = lambda: self.press("2")).grid(row = 2, column = 2, sticky = W + E)
        Button(window, text = "3", command = lambda: self.press("3")).grid(row = 2, column = 3, sticky = W + E)
        Button(window, text = "4", command = lambda: self.press("4")).grid(row = 3, column = 1, sticky = W + E)
        Button(window, text = "5", command = lambda: self.press("5")).grid(row = 3, column = 2, sticky = W + E)
        Button(window, text = "6", command = lambda: self.press("6")).grid(row = 3, column = 3, sticky = W + E)
        Button(window, text = "7", command = lambda: self.press("7")).grid(row = 4, column = 1, sticky = W + E)
        Button(window, text = "8", command = lambda: self.press("8")).grid(row = 4, column = 2, sticky = W + E)
        Button(window, text = "9", command = lambda: self.press("9")).grid(row = 4, column = 3, sticky = W + E)
        Button(window, text = "0", command = lambda: self.press("0")).grid(row = 5, column = 1, sticky = W + E)
        Button(window, text = ".", command = lambda: self.press(".")).grid(row = 5, column = 2, sticky = W + E)
        Button(window, text = "=", command = lambda: self.press("=")).grid(row = 5, column = 3, sticky = W + E)
        Button(window, text = "+", command = lambda: self.press("+")).grid(row = 2, column = 4, sticky = W + E)
        Button(window, text = "-", command = lambda: self.press("-")).grid(row = 3, column = 4, sticky = W + E)
        Button(window, text = "*", command = lambda: self.press("*")).grid(row = 4, column = 4, sticky = W + E)
        Button(window, text = "/", command = lambda: self.press("/")).grid(row = 5, column = 4, sticky = W + E)
        Button(window, text = "C", command = lambda: self.press("C")).grid(row = 6, column = 1, sticky = W + E)
        Button(window, text = "CE", command = lambda: self.press("CE")).grid(row = 6, column = 2, sticky = W + E)
        Button(window, text = "(", command = lambda: self.press("(")).grid(row = 6, column = 3, sticky = W + E)
        Button(window, text = ")", command = lambda: self.press(")")).grid(row = 6, column = 4, sticky = W + E)

        window.mainloop()

    def press(self, key):
        if key == "=":
            try:
                result = eval(self.display.get())
            except:
                result = "Error"
            self.display.set(result)
        elif key == "C":
            self.display.set("")
        else:
            self.display.set(self.display.get() + key)

Calculator()