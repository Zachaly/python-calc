import tkinter as tk
from tkinter.font import Font

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(0, 0)

        self.defaultFont = Font(family="Arial", size=24)
        self.fakeImg = tk.PhotoImage(width=1, height=1)

        self.addColums()
        self.addRows()

        self.numberLabel = tk.Label(compound="r", font=self.defaultFont)
        self.numberLabel.grid(row=0, column=0, columnspan=4, sticky=tk.E)

        currentnumber = 1
        currentrow = 1
        currentcolumn = 0
        while currentnumber <= 9:
            if(currentnumber == 4 or currentnumber == 7):
                currentrow += 1
                currentcolumn = 0
            self.numberButton(currentnumber, currentrow, currentcolumn)
            currentnumber += 1
            currentcolumn += 1
        
        self.numberButton(0, 4, 0)

    def numberButton(self, number, row, column):
        button = tk.Button(self, text=str(number),
        image=self.fakeImg,
        font=self.defaultFont,
        width=100,
        height=100,
        compound="c",
        command=lambda: self.addNumber(number)) 
        button.grid(row=row, column=column)

    def addNumber(self, number):
        self.numberLabel["text"] += str(number)

    def addColums(self):
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def addRows(self):
        for i in range(4):
            self.rowconfigure(i, weight=1)

app = App()
app.mainloop()