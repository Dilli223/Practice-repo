class Student:

    def __init__(self,name,age,department):

        self.name=name

        self.age=age

        self.department=department

    def display(self):

        print("Name :",self.name)

        print("Age :",self.age)

        print("Department :",self.department)

    def study(self):

        print(self.name,"is studying")

    def graduate(self):

        print(self.name,"graduated successfully")
