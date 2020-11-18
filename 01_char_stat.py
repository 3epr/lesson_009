# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код
import zipfile
from pprint import pprint


class CharStatFile:

    def __init__(self, file_name):
        self.file_name = file_name
        self.total = 0
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def statistic(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
                        self.total += 1

    def output(self, n):
        print('+----------+----------+')
        print(f'|{"буква":^10}|{"частота":^10}|')
        print('+----------+----------+')
        if n == 0:
            sort_list = list(self.stat.items())
            sort_list.sort(key=lambda i: i[1])
            for _ in sort_list:
                print(f'|{_[0]:^10}|{_[1]:^10}|')
        elif n == 1:
            sort_list = list(self.stat.keys())
            sort_list.sort()
            for _ in sort_list:
                print(f'|{_:^10}|{self.stat[_]:^10}|')
        elif n == 2:
            sort_list = list(self.stat.keys())
            sort_list.sort(reverse=True)
            for _ in sort_list:
                print(f'|{_:^10}|{self.stat[_]:^10}|')
        print('+----------+----------+')
        print(f'|{"итого":^10}|{self.total:^10}|')
        print('+----------+----------+')


wip = CharStatFile('voyna-i-mir.txt.zip')
wip.statistic()
wip.output(1)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828