from person import Person

class Employee(Person):

    def __init__(self, first_name, last_name, age, position, salary):
        super().__init__(first_name, last_name, age)
        self.postion = position
        self.salary = salary

    @property
    def position(self):
        return self.postion

    @position.setter
    def position(self, value):
        self.postion = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError('Salary should be higher than zero.')

        self.__salary = value

    def introduction(self):
        introduction = super().introduce()
        introduction += f" I am {self.postion}."
        return introduction