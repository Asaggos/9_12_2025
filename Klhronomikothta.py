class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def printStats(self):
        print(self.name, self.age)

class Teacher(Person):
    def __init__(self,name,age,salary,xronia):
        Person.__init__(name,age)
        self.salary = salary
        self.xronia = xronia

class Student(Person):
    def __init__(self, name, age, AM):
        super().__init__(name, age)
        self.AM = AM

    def getAM(self):
        print(self.AM)

mathitis = Student("Nikos",25,144)
mathitis.printStats(), mathitis.getAM()