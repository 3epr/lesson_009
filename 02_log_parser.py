# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint


class LogAnalizator:
    def __init__(self, inputf, outputf=None):
        self.name = inputf
        self.out = outputf
        self.st = {}

    def sbor_stat(self, n=17):
        with open(self.name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[1:n] in self.st and line[29:-1] == 'NOK':
                    self.st[line[1:n]] += 1
                elif line[29:-1] == 'NOK':
                    self.st[line[1:n]] = 1

    def output(self, n=0):
        if n == 0:
            self.sbor_stat()
        elif n == 1:
            self.sbor_stat(14)
        elif n == 2:
            self.sbor_stat(8)
        elif n == 3:
            self.sbor_stat(5)
        if self.out == None:
            pprint(self.st)
        else:
            file = open(self.out, 'w', encoding='utf8')
            for _ in self.st:
                lin = f'[{_}] {self.st[_]}\n'
                file.writelines(lin)
            file.close()

first = LogAnalizator('events.txt', 'out.txt')
first.output(0)

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
