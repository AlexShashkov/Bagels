import random

class Guess():
    def __init__(self, digits: int, max_g: int):
        numbers = list(range(10))
        self.number = ''
        for i in range(digits):
            self.number += str(numbers[random.randrange(10)])
        self.tries = 0
        self.max_tries = max_g
        self.status = True

    def __call__(self, x):
        if not self.status:
            raise("Игра уже была закончена")
        clues = []
        if x == self.number:
            self.status = False
            return [True, "Вы угадали число!"]
        if len(x) != len(self.number):
            return ["Размер числа не совпадает с заданным!"]
        allnumbers = list(self.number)
        for (inp, check) in zip(list(x), allnumbers):
            if inp == check:
                clues.append("Fermi")
            elif inp in allnumbers:
                clues.append("Pico")
        if len(clues) == 0:
            clues.append("Bagels")
        self.tries += 1
        if self.tries > self.max_tries:
            self.status = False
            clues.insert(0, False)
            return clues
        clues.insert(0, "NG")
        return clues
