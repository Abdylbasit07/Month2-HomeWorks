import random
from random import randint
class Person():
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'I am {self.fullname}, my age: {self.age}, my status: {self.is_married}')


class Student(Person):
    marks = {
        "eng": 4,
        'rus': 5,
        "math": 5,
    }

    def math_mid(self):
        res = 0
        count = 0
        for v in self.marks.values():
            res += v
            count += 1
        return res / count


class Teacher(Person):
    def __init__(self, fullname, age, is_married, salary, experience):
        super().__init__(fullname, age, is_married)
        self.salary = salary
        self.experience = experience

    def full_salary(self):
        if self.experience > 3:
            self.salary += self.salary * 0.05
        print(self.salary)


def create_students():
    res = []
    for i in range(3):
        na = random.randint(1, 4)
        if na == 1:
            na = "Vladimir Putin"
        elif na == 2:
            na = "Soronbay Jeenbekov"
        elif na == 3:
            na = "Ysakov Emir"
        elif na == 4:
            na = "Uzakov Daud"
        else:
            pass
        ag = random.randint(12, 19)
        a = Student(na, ag, True)
        res.append(a)
    return res


for i in create_students():
    i.introduce_myself()
    print(i.math_mid())

stud1 = Person("Zhorobekov Abu ", 15, False)

teach = Teacher("Jordj Vashington", 43, False, 45000, 17)

stud1.introduce_myself()

teach.full_salary()
teach.introduce_myself()
create_students()
