# class dog:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age  
#         pass
# d1 = dog("bruno",22)
# d2 = dog("cref",12)
# print(d1.name)
# print(d2.name)

# class car:
#     brand='audi'

#     def __init__ (self,brand, model , year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def displayinfo(self):
#         print(self.brand)
#         print(self.model)
#         print(self.year)

# print(car.brand)
# c=car("ford","mustang",1999)
# c.displayinfo()

#  Create a class Vehicle with a method start_engine() that prints "Engine started".

# class vehicle():

#     def start_engine(self):
#         print("start engine")
#     def fueltype(self):
#         return "petrol"

# #Create a Car class that inherits from Vehicle and has its own method honk().

# class car(vehicle):
#     def honk(self):
#         print("honk")
# d = car()
# d.honk()
# d.start_engine()


# class electriccar(vehicle):
#     def fueltype(self):
#         return "electric"

# e = electriccar()
# v = vehicle()
# print(e.fueltype())
# print(v.fueltype())

class animal():
    def __init__(self,name):
        self.name = name
        pass
class dog(animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
        pass
a = dog("bruno","german dog")
print("animal name is " + a.name + " and its a "+a.breed)