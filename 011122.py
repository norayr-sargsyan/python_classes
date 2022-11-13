from _datetime import datetime
import typing


class Human:
    current_year = datetime.now().year

    def __init__(self, name: str, surname: str, age: int, height: int, weight: int, gender: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

    def year_minus(self) -> str:
        """
        This method which will tel in which year the person will be 100 years old:
        :return: str
        """
        return f"You will be 100 years old {self.current_year - self.age + 100}։"

    def optimal_weight(self) -> str:
        """
        This method tell the optimal weight:
        :return: str
        """

        if self.gender[0].upper() == "F" or self.gender.upper() == "MAN":
            result = (self.height - 100) * 1.15
        else:
            result = (self.height - 110) * 1.15
        return f"Your optimal weight is {result} but your weight {self.weight}։"

    def present(self) -> str:
        """
        This method is for presentation:
        :return: str
        """

        return f"Name: {self.name}\nSurname: {self.surname}\nGender: {self.gender}\nAge: {self.age}\nHeight: {self.height}\nWeight: {self.weight} "


# john = Human("John", "Don", 26, 170, 68, "Female")
#
# print(john.present())
# print(john.optimal_weight())
# print(john.year_minus())


class Student(Human):

    def __init__(self, marks: list, name: str, surname: str, age: int, height: int, weight: int, gender: str):
        self.marks = marks
        super().__init__(name, surname, age, height, weight, gender)

    def add_mark(self, *mark: int) -> str:
        """
        This method added marks in mark list student/
        :param mark: int
        :return: str
        """
        for i in mark:
            self.marks.append(i)
        return f"Added marks {self.marks}"

    def mog(self) -> typing.Union[int, float, complex]:
        """
        This method calculate the average mark.
        :return: int, float, complex
        """
        sum_marks = 0
        for i in self.marks:
            sum_marks += i
        mog = sum_marks / len(self.marks)


        return mog

    def present_student(self) -> str:
        """
        This method is for presentation:
        :return: str
        """
        return f"{self.present()}\nMarks: {self.marks}\nAverage score: {self.mog()}"

# john = Student([80, 90, 55], "John", "Don", 19, 169, 60, "Female")
#
# print(john.present_student())
# print(john.add_mark(49, 100, 79))
# print(john.present_student())
