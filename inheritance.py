class Person:

    def __init__(self, name, age, salary) -> None:
        self.name= name
        self.age = age
        self.salary = salary


    def __str__(self) -> str:
        return f'Name : {self.name}\tage : {self.age}\tSalary : {self.salary}'

    def __repr__(self) -> str:
        return f'Name : {self.name}\tage : {self.age}\tSalary : {self.salary}'


class Teacher(Person):

    def __init__(self, name, age, subject, salary) -> None:
        super().__init__(name, age, salary)
        self.subject = subject

    def __str__(self) -> str:
        return f'Name : {self.name}\tage : {self.age}\tSubject : {self.subject}\tSalary : {self.salary}'

    def __repr__(self) -> str:
        return f'Name : {self.name}\tage : {self.age}\tSubject : {self.subject}\tSalary : {self.salary}'

class Doctor(Person):

    def __init__(self, name, age, speciality, salary) -> None:
        super().__init__(name, age, salary)
        self.speciality = speciality

    def __str__(self) -> str:
        return f'Name : {self.name}\tage : {self.age}\tspeciality : {self.speciality}\tSalary : {self.salary}'

    def __repr__(self) -> str:
        return f'Name : {self.name}\tage : {self.age}\tspeciality : {self.speciality}\tSalary : {self.salary}'



def main():
    Rahul = Teacher('Rahul', '25','Maths','50000')
    print(Rahul)

    Riya = Doctor('Riya', '31', 'Dentist', '55000')
    print(Riya)


if __name__=='__main__':
    main()