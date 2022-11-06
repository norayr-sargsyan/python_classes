class Triangle:
    sum_1 = 0

    def __new__(cls, *args, **kwargs):
        cls.sum_1 += 1

        return super().__new__(cls)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sort_size_tuple(self):
        return sorted((self.a, self.b, self.c))

    def __eq__(self, new_triangle):
        for i in range(3):
            if self.sort_size_tuple()[i] != new_triangle.sort_size_tuple()[i]:
                return False
        return True

    def is_alike_per(self, other):
        if sum((self.a, self.b, self.c)) == sum(other):
            return True
        return False

    def is_alike_area(self, other):
        p_1 = sum((self.a, self.b, self.c)) / 2
        p_2 = sum(other) / 2
        area_1 = (p_1 * (p_1 - self.a) * (p_1 - self.b) * (p_1 - self.c)) ** 0.5
        area_2 = (p_2 * (p_2 - other[0]) * (p_2 - other[1]) * (p_2 - other[2])) ** 0.5
        if area_1 == area_2:
            return True
        return False


c1 = Triangle(1, 2, 3)
c2 = Triangle(2, 3, 1)
# print(c1.is_alike_per(c2))
# print(c1.is_alike_area(c2))
print(c1 == c2)


class Rectangular:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sort_size(self):
        return sorted((self.a, self.b))

    def __eq__(self, other):
        for i in range(2):
            if self.sort_size()[i] != other.sort_size()[i]:
                return False
        return True

    def __gt__(self, other):
        if other.sort_size()[-1] < self.sort_size()[-1]:
            return True
        return False



