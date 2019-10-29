import random


class Lexeme: # класс лексема, слово из словаря, аргумент лексической функции
    def __init__(self, lemma, pos, definition):
        self.lemma = lemma              # string - начальная форма слова
        self.pos = pos                  # string - часть речи, S - существительное, A - прилагательное, V - глагол, ADV - наречие, NUM - числительное, PR - предлог
        self.definition = definition    # string - толкование
        self.lfValues = dict()          # dict - список-словарь значений лексических функций у данной лексемы, каждый элемент содержит объект лексическую функцию и множество значений (функции могут быть многозначны)

    def add_lf_value(self, lf, value):    # добавляет значение лексической функции
        if lf not in self.lfValues:   # если такой лексической функции ещё нет в списке
            self.lfValues[lf] = set() # создаём пустое множество значений

        if value not in self.lfValues[lf]:    # если значения ещё нет в множестве значений
            self.lfValues[lf].add(value)      # добавляем значение в множество значений
            lf.add_lexeme_value(self, value)  # добавляем лексему в список лексем у самой лексической функции

    def __str__(self): # преобразует объект лексему в строку для вывода на экран
        text = self.lemma + ", " + self.pos + ", " + self.definition
        for (lf, values) in self.lfValues.items():
            text += "\n  " + lf.name + "() = " + str(values)
        return text + "\n"


class LexicalFunction: # класс лексическая функция
    def __init__(self, name, definition):
        self.name = name                # string - название лексической функции
        self.definition = definition    # string - определение-толкование
        self.lexemeValues = dict()      # dict - список-словарь лексем, у которых определена данная лексическая функция, каждый элемент содержит объект лексему и множество значений (функции могут быть многозначны)

    def add_lexeme_value(self, lexeme, value): # добавляет значение ЛФ для лексемы
        if lexeme not in self.lexemeValues:      # если такой лексемы ещё нет в списке
           self.lexemeValues[lexeme] = set()     # создаём пустое множество значений

        if value not in self.lexemeValues[lexeme]:   # если значения ещё нет в множестве значений
            self.lexemeValues[lexeme].add(value)     # добавляем значение в множество значений
            lexeme.add_lf_value(self, value)         # добавляем лекксическую функцию в лексему

    def __str__(self): # преобразует объект лексическую функцию в строку для вывода на экран
        text = self.name + ", " + self.definition
        for lexeme, values in self.lexemeValues.items():
            text += "\n  f(" + lexeme.lemma + ") = " + str(values)
        return text + "\n"


def lm_and_lf():                # преобразование всех лексем и функций объединено в функцию, чтобы использовать в файле myproject.py
    lexemes = dict()            # список-словарь всех лексем, каждый элемент содержит лемму (начальную форму слова) и объект-лексему
    lexicalFunctions = dict()   # список-словарь лексических функций, каждый элемент сожержит название лексической функции и объект лексическую функцию

    file = open("lexemes.txt", 'r', encoding='utf-8') # читаем список лексем из файла
    for line in file.read().splitlines():
        (lemma, pos, definition) = line.split("\t")
        lexeme = Lexeme(lemma, pos, definition)
        lexemes[lemma] = lexeme
    file.close()

    file = open("lfs.txt", 'r', encoding='utf-8') # читаем список лексических функций из файла
    for line in file.read().splitlines():
        (name, definition) = line.split("\t")
        lf = LexicalFunction(name, definition)
        lexicalFunctions[name] = lf
    file.close()

    file = open("lf_values.txt", 'r', encoding='utf-8') # читаем список значений лексических функций из файла
    for line in file.read().splitlines():
        (lemma, lfName, value) = line.split("\t")
        lexeme = lexemes[lemma]
        lf = lexicalFunctions[lfName]
        lexeme.add_lf_value(lf, value)
    file.close()
    return lexicalFunctions

# тестовый вывод для примера
#print (lexemes["КЛУБ"])


