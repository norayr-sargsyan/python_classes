import typing
from random import randint


class DictMake:
    def __init__(self, dict_str):
        self.makedict = dict_str

    def make(self):
        dict_ = {}
        for k in self.makedict:
            rand_1 = randint(0, 9)
            dict_[k] = rand_1
        return dict_

    def duplicate_remove(self):
        dict_1 = self.make()
        list_1 = []
        dict_2 = {}
        for i in dict_1:
            if dict_1[i] not in list_1:
                list_1.append(dict_1[i])
                dict_2[i] = dict_1[i]
        return dict_2

    def max_tree_value(self):

        dict_2 = self.duplicate_remove()
        new_dict = {}
        for max_1 in range(0, 3):
            max_1 = -1
            k = ""
            for i in dict_2:
                if dict_2[i] > max_1:
                    max_1 = dict_2[i]
                    k = i

            dict_2.pop(k)
            new_dict[k] = max_1

        return new_dict


class Circle:
    def __init__(self, rad: typing.Union[int, float]):
        self.rad = rad

    def area(self):
        pe = 3.14
        s = pe * self.rad ** 2
        return s

    def perimetr(self):
        pi = 3.14
        perimetr = 2 * pi * self.rad

        return perimetr
