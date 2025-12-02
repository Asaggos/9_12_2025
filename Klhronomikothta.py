class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age

class Teacher(Person):
    def __init__(self,name,age,salary,xronia):
        Person.__init__(name,age)
        self.salary = salary
        self.xronia = xronia
