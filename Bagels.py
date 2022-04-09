import random

class Guess():
    '''
    Функтор игры
    @param digits: Длина загадонного числа
    @param max_g: Количество попыток
    '''
    def __init__(self, digits: int, max_g: int):
        numbers = list(range(10))
        self.number = ''
        # Генерируем число
        for i in range(digits):
            self.number += str(numbers[random.randrange(10)])
        # Счеткик попыток, статус игры
        self.tries = 0
        self.max_tries = max_g
        self.status = True

    '''
    Непосредственно реализация функтора
    @param input: Входная строка
    @return: Возвращает кортеж, который включает в себя:
        1. Состояние:
            True - Игра выиграна
            False - Игра окончена
            "NG" - Слово не было угадано
        2. Подсказки
    '''
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
        # Посимвольный перебор
        for (inp, check) in zip(list(x), allnumbers):
            if inp == check:
                # Символ совпадает
                clues.append("Fermi")
            elif inp in allnumbers:
                # Сивол не совпадает, но имеется в другом месте
                clues.append("Pico")
        if len(clues) == 0:
            # Ни один символ не совпал и его нет в другом месте
            clues.append("Bagels")
        self.tries += 1
        if self.tries > self.max_tries:
            # Проигрышь
            self.status = False
            clues.insert(0, False)
            return clues
        clues.insert(0, "NG")
        return clues

    def Get(self):
        return self.number
