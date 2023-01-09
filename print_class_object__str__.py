class Person:

    def __init__(self, name, occupation, salary) -> None:
        self.name= name
        self.occupation = occupation
        self.salary = salary


    def __str__(self) -> str:
        return f'Name : {self.name}\tOccupation : {self.occupation}\tSalary : {self.salary}'

    def __repr__(self) -> str:
        return f'Name : {self.name}\tOccupation : {self.occupation}\tSalary : {self.salary}'


class Teacher(Person):

    def __init__(self, name, occupation, subject, salary) -> None:
        super().__init__(name, occupation, salary)
        self.subject = subject

    def __str__(self) -> str:
        return f'Name : {self.name}\tOccupation : {self.occupation}\tSubject : {self.subject}\tSalary : {self.salary}'

    def __repr__(self) -> str:
        return f'Name : {self.name}\tOccupation : {self.occupation}\tSubject : {self.subject}\tSalary : {self.salary}'

class Doctor(Person):

    def __init__(self, name, occupation, speciality, salary) -> None:
        super().__init__(name, occupation, salary)
        self.speciality = speciality

    def __str__(self) -> str:
        return f'Name : {self.name}\tOccupation : {self.occupation}\speciality : {self.speciality}\tSalary : {self.salary}'

    def __repr__(self) -> str:
        return f'Name : {self.name}\tOccupation : {self.occupation}\tspeciality : {self.speciality}\tSalary : {self.salary}'



def main():
    Rahul = Teacher('Rahul', 'Teacher','Maths','50000')
    print(Rahul)

    Riya = Doctor('Riya', 'Doctor', 'Dentist', '55000')
    print(Riya)


if __name__=='__main__':
    main()