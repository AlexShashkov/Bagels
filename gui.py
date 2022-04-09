import tkinter as tk
from Bagels import Guess

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.scrollbar = tk.Scrollbar()
        self.scrollbar.pack(side = tk.RIGHT, fill=tk.Y)
        self.list = tk.Listbox(yscrollcommand = self.scrollbar.set)

        self.list.insert(tk.END, "Привет, давай поиграем в Bagels")
        self.inp = tk.Entry(width=10)
        self.btn = tk.Button(text="Ввод")


        self.list.insert(tk.END, "Введи сколько знаков должно быть в числе")
        self.list.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)
        self.inp.pack(fill=tk.X)
        self.btn.pack(fill=tk.X)

        self.status = "DIGITS"
        self.Game = None
        self.max_tries = None
        self.digits = None

        self.inp.bind('<Key-Return>', self.handleInput)

        # Функции при вводе
        self.funcs = {}
        self.funcs["DIGITS"] = self.getdigits
        self.funcs["TRIES"] = self.getTries
        self.funcs["GAME"] = self.guess

    def handleInput(self, event):
        print(self.status)
        self.funcs[self.status](event)

    def getdigits(self, event):
        self.digits = int(self.inp.get())
        self.list.insert(tk.END, f"В числе будет {self.digits} знаков. Введи количество попыток.")
        self.status = "TRIES"

    def getTries(self, event):
        self.max_tries = int(self.inp.get())
        self.list.insert(tk.END, f"У тебя есть {self.max_tries} попыток. Введи число!")
        self.Game = Guess(self.digits, self.max_tries)
        self.status = "GAME"

    def guess(self, event):
        number = self.inp.get()
        result = self.Game(number)
        status = result[0]

        if status == "NG":
            string = f"Не угадал! {result[1:]}"
            self.list.insert(tk.END, string)
        elif status == False:
            string = f"Игра окончена. Загаданное число: {self.Game.Get()}"
            self.list.insert(tk.END, string)
            self.list.insert(tk.END, "Введи сколько знаков должно быть в числе")
            self.status = "DIGITS"
        elif status == True:
            string = "Вы выиграли!"
            self.list.insert(tk.END, string)
            pass
        else:
            self.list.insert(tk.END, result[0])

        print(result)

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
