class Person:

    def __init__(self, name, age, salary) -> None:
        self.name= name
        self.age = age
        self.salary = salary


    def __str__(self) -> str:
        return f'Name : {self.name}\tage : {self.age}\tSalary : {self.salary}'

    def __repr__(self) -> str:
        return f'Name : {self.name}\tage : {self.age}\tSalary : {self.salary}'



def main():
    Rahul = Person('Rahul', '25','50000')
    print(Rahul)


if __name__=='__main__':
    main()