import tkinter as tk
from tkinter.font import Font

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(0, 0)
        self.calcSign = ""
        self.defaultFont = Font(family="Arial", size=24)
        self.fakeImg = tk.PhotoImage(width=1, height=1)

        self.addColums()
        self.addRows()

        self.previusNumber = 0
        self.previusNumberLabel = tk.Label(compound="r", font=Font(family="Arial", size=16), text=str(self.previusNumber))
        self.previusNumberLabel.grid(row=0, column=0, columnspan=4, sticky=tk.E)

        self.numberLabel = tk.Label(compound="r", font=self.defaultFont)
        self.numberLabel.grid(row=1, column=0, columnspan=4, sticky=tk.E)

        currentnumber = 1
        currentrow = 2
        currentcolumn = 0
        while currentnumber <= 9:
            if(currentnumber == 4 or currentnumber == 7):
                currentrow += 1
                currentcolumn = 0
            self.numberButton(currentnumber, currentrow, currentcolumn)
            currentnumber += 1
            currentcolumn += 1
        
        self.numberButton(0, 5, 0)

        self.defaultButton(".", self.addDot, 5, 1)
        self.defaultButton("del", self.deleteNum, 5, 2)
        self.defaultButton("+", lambda: self.setCalcSign("+"), 2, 3)
        self.defaultButton("-", lambda: self.setCalcSign("-"), 3, 3)
        self.defaultButton("/", lambda: self.setCalcSign("/"), 4, 3)
        self.defaultButton("*", lambda: self.setCalcSign("*"), 5, 3)
        self.defaultButton("=", self.equals, 6, 0)

    def numberButton(self, number, row, column):
        return self.defaultButton(str(number), lambda: self.addNumber(str(number)), row, column)

    def defaultButton(self, text, command, row, column):
        button = tk.Button(self, text=text,
        image=self.fakeImg,
        font=self.defaultFont,
        width=100,
        height=100,
        compound="c",
        command=command)

        button.grid(row=row, column=column)

        return button

    def addNumber(self, number):
        self.numberLabel["text"] += number

    def addColums(self):
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def addRows(self):
        for i in range(6):
            self.rowconfigure(i, weight=1)

    def addDot(self):
        if "." in self.numberLabel["text"]:
            return
        if len(self.numberLabel["text"]) == 0 :
            self.numberLabel["text"] += "0"
        self.numberLabel["text"] += "."
    
    def deleteNum(self):
        if len(self.numberLabel["text"]) == 0:
            return
        
        self.numberLabel["text"] = self.numberLabel["text"][:-1]

    def setCalcSign(self, sign):
        self.previusNumber = float(self.numberLabel["text"])
        self.previusNumberLabel["text"] = str(self.previusNumber)
        self.numberLabel["text"] = ""
        self.calcSign = sign

    def equals(self):
        number = float(self.numberLabel["text"])

        if self.calcSign == "+":
            self.numberLabel["text"] = str(self.previusNumber + number)
        elif self.calcSign == "-":
            self.numberLabel["text"] = str(self.previusNumber - number)
        elif self.calcSign == "*":
            self.numberLabel["text"] = str(self.previusNumber * number)
        elif self.calcSign == "/":
            self.numberLabel["text"] = str(self.previusNumber / number)
        
        self.previusNumberLabel["text"] = str(number)

app = App()
app.mainloop()
