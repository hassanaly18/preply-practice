class Payment:
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("paid using credit card")

class Paypal(Payment):
    def pay(self):
        print("Paid using paypal")

class Cash(Payment):
    def pay(self):
        print("paid using cash")

payments = [CreditCard(), Paypal(), Cash()]                           

for p in payments:
    p.pay()



























# class Bird:
#     def fly(self):
#         print("bird is flying")

# class Airplane:
#     def fly(self):
#         print("Airplane is flying")

# class Car:
#     def move(self):
#         print("Car is moving")

# def startFlyng(obj):
#     obj.fly()

# b = Bird()
# a = Airplane()
# c = Car()

# startFlyng(b)
# startFlyng(a)












# class Vehicle:
#     def move(self):
#         print("vehicle is moving..")

# class Plane(Vehicle):
#     def move(self):
#         print("Plane is moving")
        
# class Car(Vehicle):
#     def move(self):
#         print("Car is moving")

# vehicles = [Car(), Plane()]

# for v in vehicles:
#     v.move()












# class Dog:
#     def sound(self):
#         print("Barks")

# class Cat:
#     def sound(self):
#         print("meow")
        
# def makeSound(animal):
#     animal.sound()  
    
# d = Dog()
# c = Cat()

# makeSound(d)
# makeSound(c)                  