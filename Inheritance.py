class School:
    def Classes(self):
        print("In Class")


class Student(School):
    pass


some=Student()
some.Classes()
