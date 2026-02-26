class GrandParent():
    def home(self):
        print("I own a home")
        
class Parent(GrandParent):
    def car(self):
        print("I own a car")

class Child(Parent):
    def bike(self):
        print("I own a bike")        

g = GrandParent()
p =Parent()
c = Child()


















class Animal:
    def sound(self):
        print("ANimal is making some sound")

class Dog(Animal):
    def sound(self):
        print("barking..")  

# a1 = Animal()
# d1 = Dog()

#method overriding
# d1.sound()


























class Person:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print("The person's name:", self.name)

class Student(Person):
    def __init__(self, name, roll):
         super().__init__(name) 
         self.roll = roll          

    def show(self):
        print("Student Info..")
        super().show()
        print("Roll No:", self.roll)  

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject      
    
    def show(self):
        print("Teacher Info..")
        super().show()
        print("Subject:", self.subject) 
        
# s1 = Student("Mike", 786)
# s1.show()        





















class Vehicle:
    def start(self):
        print("Vehicle is starting...")
    
    def stop(self):
        print("Vehicle is stopping...")    

class Car(Vehicle):
    def drive(self):
        print("Car is driving")
        
# c1 = Car()

# c1.drive()        
# c1.start()
# c1.stop()