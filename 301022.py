from random import randint




class DictMake:
    def __init__(self, dict_str):
        self.makedict = dict_str

    def make(self):
        dict_ = {}
        for k in self.makedict:
            rand_1 = randint(0, 9)
            dict_[k] = rand_1

    def duplicate_remove(self):
        dict_1 = {}
        for k in self.makedict:
            rand_2 = randint(0, 9)
            dict_1[k] = rand_2
        tuple_1 = ()
        dict_2 = {}
        for i in dict_1:
            if dict_1[i] not in tuple_1:
                tuple_1 += (dict_1[i], )
                dict_2[i] = dict_1[i]
        print(dict_2)

# DictMake_1 = DictMake("pyton")
#
# DictMake_1.duplicate_remove()
    def max_tree_value(self):
        dict_1 = {}
        for k in self.makedict:
            rand_2 = randint(0, 30)
            dict_1[k] = rand_2
        tuple_1 = ()
        dict_2 = {}
        for i in dict_1:
            if dict_1[i] not in tuple_1:
                tuple_1 += (dict_1[i],)
                dict_2[i] = dict_1[i]
        max_1 = -1
        k = ""
        new_dict = {}
        for i in dict_2:
            if dict_2[i] > max_1:
                max_1 = dict_2[i]
                k = i

        dict_2.pop(k)
        new_dict[k] = max_1

        max_1 = -1
        k = ""
        for i in dict_2:
            if dict_2[i] > max_1:
                max_1 = dict_2[i]
                k = i

        dict_2.pop(k)
        new_dict[k] = max_1

        max_1 = -1
        k = ""
        for i in dict_2:
            if dict_2[i] > max_1:
                max_1 = dict_2[i]
                k = i

        dict_2.pop(k)
        new_dict[k] = max_1

        print(new_dict)




DictMake_1 = DictMake("abcdefjh")

DictMake_1.max_tree_value()
