class Student:
    # class variables
    total_students = 0
    all_students = []
    GENDER = ["Male", "Female"]

    # for everytime we create an instance, update the all_students array to include the instance you just created

    def __init__(self, first_name, last_name, gender, course, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.course = course
        self.age = age
        Student.total_students += 1
        Student.all_students.append(self)

    # instance methods
    # getter method
    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    @property
    def first_name(self):
        return self._first_name

    # setter method
    @first_name.setter
    def first_name(self, name_input):
        if isinstance(name_input, str):
            self._first_name = name_input

        else:
            raise ValueError("First name must be of type string")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender_input):
        formatted_input = gender_input.capitalize()
        if isinstance(formatted_input, str):
            if formatted_input in Student.GENDER:
                self._gender = formatted_input
            else:
                raise ValueError(
                    f"Gender must be either {Student.GENDER[0]} or {Student.GENDER[1]}"
                )
        else:
            raise ValueError("Gender must be of type string")

    @classmethod
    def all_male_students(cls):
        return [
            student.fullname()
            for student in cls.all_students
            if student.gender == "Male"
        ]

    @classmethod
    def all_female_students(cls):
        return [
            student.fullname()
            for student in cls.all_students
            if student.gender == "Female"
        ]

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def print_self(self):
        return self

    # method to verify age of student
    # @property
    # def age(self):
    #     return self._age

    # @age.setter
    # def age(self, age_input):
    #     if age_input >= 18:
    #         self._age = age_input
    #     else:
    #         raise ValueError("Not Elligible")

    def is_age_eligible(self):
        # return True if self.age > 18 else False
        if self.age < 18:
            return False
        else:
            return True

    def __repr__(self):
        return str(self.__dict__)


student1 = Student("Frank", "Mwangi", "Male", "Software Engineering", 17)
student2 = Student("Brian", "Ngoyoni", "Male", "Software Engineering", 25)
student3 = Student("Calvin", "Cheptoo", "Female", "Software Engineering", 18)
student4 = Student("Jeremy", "Leannan", "Male", "Software Engineering", 22)
student5 = Student("John", "Kamau", "Male", "Software Engineering", 23)
student6 = Student("Caleb", "Mwaniki", "Male", "Software Engineering", 20)
student7 = Student("Faith", "Kamande", "Female", "Software Engineering", 23)
student8 = Student("Janet", "Moraa", "Female", "Software Engineering", 20)
student9 = Student("Collins", "Koome", "Male", "Software Engineering", 23)
student10 = Student("Jadyn", "Wanja", "Female", "Software Engineering", 19)


# print(student2.__dict__)


# access the email of student 1 and student 3
# print(student1.email)
# print(Student.total_students)
# print(Student.all_students)


# print(Student.all_male_students())
# print(Student.all_female_students())


print(student1.print_self())

print(student1.is_age_eligible())
print(student10.is_age_eligible())
