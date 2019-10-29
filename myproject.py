import random
import lexy as lx

class MyException(Exception):
    pass

class Game_Session():  # класс для лексической игры
    def __init__(self, LF, lexical_function=None, argument=None, example=None):
        self.LF = LF
        self.lexical_function = lexical_function
        self.argument = argument
        self.example = example


    def lx_random_choice(self):  # функция для случайного выбора лексической функции и ее аргумента
        lexical_function = random.choice(list(self.LF.keys()))
        arg = list(self.LF[lexical_function].lexemeValues.keys())
        while not len(arg):
            lexical_function = random.choice(list(self.LF.keys()))
            arg = list(self.LF[lexical_function].lexemeValues.keys())
        argument = random.choice(arg).lemma
        self.lexical_function = lexical_function
        self.argument = argument
        self.find_examples()
        return lexical_function, argument

    def find_examples(self):  # запись всех примеров в массив self.example
        self.example = set()
        lx = list(self.LF[self.lexical_function].lexemeValues)
        for l in lx:
            for k in l.lfValues:
                if k.name == self.lexical_function and l.lemma != self.argument:
                    self.example.add((l.lemma, ', '.join(l.lfValues[k])))

    def one_example(self):  # возвращение пользователю примераа и удаление этого примера из массива
        if self.argument is None or self.lexical_function is None:
            raise MyException("Выберите вначале лексическую функцию")
        else:
            if len(self.example) == 0:
                return None
            else:
                ex = self.example.pop()
                return ex


    def lfDefinition(self):  # значение заданной лексической функции
        if self.argument is None or self.lexical_function is None:
            raise MyException("Выберите вначале лексическую функцию")
        else:
            return self.LF[self.lexical_function].definition

    def answer_to_normal(self, correct):  # выбор из корректного ответа на лексическую функцию ключевых слов, по которым потом сверяется ответ
        ans = correct.split()
        words = set()
        for a in ans:
            if a[0] != "(":
                words.add(a.rstrip(">").strip("<"))
        return words

    def answer_check(self, answer):  # проверка введенного пользователем ответа
        if self.argument is None or self.lexical_function is None:
            raise MyException("Выберите вначале лексическую функцию")
        else:
            lx = self.LF[self.lexical_function].lexemeValues
            ans = set()
            for l in list(lx):
                if l.lemma == self.argument:
                    correctanswer = lx[l]
                    for ca in correctanswer:
                        ans.update(self.answer_to_normal(ca))
                    break
            if answer in ans:
                return True
            return False


    def correct_answer(self):  # вывод правильного ответа
        if self.argument is None or self.lexical_function is None:
            raise MyException("Выберите вначале лексическую функцию")
        else:
            lx = self.LF[self.lexical_function].lexemeValues
            correctanswer = set()
            for l in list(lx):
                if l.lemma == self.argument:
                    correctanswer = lx[l]
            return correctanswer



g = Game_Session(lx.lm_and_lf())
#print(g.one_example())
print(g.lx_random_choice())
print(g.correct_answer())
print(g.one_example())
print(g.one_example())
print(g.lfDefinition())
print(g.one_example())

