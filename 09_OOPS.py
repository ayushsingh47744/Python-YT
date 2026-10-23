#class: A blueprint for creating objects. It defines attributes and methods that the objects will have.
#created with a word class followed by the class name and a colon.
# class Person:
#     print("hello shemdi")



# class Factory:
#     a = 12  # attribute

#     def hello(self):  #method
#         print("how are you")

#         print("hello how are you")

# print(Factory().a)

# Factory().hello()


# Object: An instance(bache) of a class.
# It is created using the class constructor and can access the attributes and methods defined in the class.
# Calling a class using () creates an object of that class.
# class Factory:
#     def __init__(self, material, zips, pockets): #Constructor: A special method that is automatically called when an object is created
#         self.material = material  # 100.material = leather (let say reebok 100 location pr stored he memory me)
#         self.zips = zips    # 100.zips = 3
#         self.pockets = pockets    # 100.pockets = 2

#     def show(self):
#         print(f"material is {self.material} and zips are {self.zips} and pockets are {self.pockets}")
# # so jo bhi hum location dete he voh self ke andr jati he aur self usko store kr leta he 
# # To target the objects location we use self keyword.
# reebok = Factory("leather", 3, 2)  # Object: reebok
# reebok.show()


# class Animal:
#     name = "lion"  # class attribute

#     def __init__(self, age):
#         self.age = age  # instance attribute

#     def show(self):  # instance method
#         print(f"how are you your age is {self.age}")

#     @classmethod
#     def hello(cls): # cls class ki location ko target krta he
#         print("how are you brother")


#     @staticmethod
#     def static():  # static method
#         print("how are you brother")

# obj = Animal(5)  # Object: obj
# obj.show()  # calling instance method
# obj.hello()  # calling class method
# obj.static()  # calling static method


# Constructor: A constructor is created inside a class using the __init__() method
# class Factory:
#     def __init__(self, material, price): #defines constructor with parameters material and price
#         self.material = material  #stores materials in object
#         self.price = price

# obj = Factory("leather", 1000)   #create an object and automatically call the constructor
# Remember:__init__() is automatically called when an object is created.
#          self refers to the current object.
#          material and price receive values from the object creation.
# In short: We create a constructor using def __init__(self): inside a class.


#Inheritance: child class inherit properties of parent class
# isme hum jo child class create krte he usme parameter ko accept nhi krte he directly kisi ek class ko accept krte he 

# class Factorymumbai:  # parent class / superclass
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")

# class Factorypune(Factorymumbai):  # child class / subclass
#     pass

# obj = Factorymumbai()
# obj2 = Factorypune()

# print(obj2.hello())

# Using constructor
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Animal name is {self.name}")

# class Human(Animal): #child class
#     pass

# animal1 = Animal("Lion")
# human1 = Human("John")
# animal1.show()  # Output: Animal name is Lion
# human1.show()   # Output: Animal name is John

# agar mereko human ki age bhi chahieye to hume constructor ko initialize krna hoga human class me
# and constructor me super() ka use krna hoga taki parent class ke constructor ko call kr sake means super class se hum jo uske uper wala parent function hoga uske attributes ko access lrte he

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Animal name is {self.name},{self.age}")

# class Human(Animal): #child class
#     def __init__(self, name, age):
#         super().__init__(name) # Call the parent class constructor
#         self.age = age

# animal1 = Animal("Lion")  # in animale there is no age so it will give error if we try to print age in animal class 
# human1 = Human("John", 30)

# animal1.show()  # Output: Animal name is Lion
# human1.show()   # Output: Animal name is John, 30

# # so whenever we create a child class and we want to add more attributes to it then we have to write that function in child class as well 
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Animal name is {self.name}")

# class Human(Animal): #child class
#     def __init__(self, name, age):
#         super().__init__(name) # Call the parent class constructor
#         self.age = age
#     def show(self):
#         print(f"Animal name is {self.name},{self.age}")

# animal1 = Animal("Lion") 
# human1 = Human("John", 30)

# animal1.show()  # Output: Animal name is Lion
# human1.show()   # Output: Animal name is John, 30





# Prev all are single level inheriance and in multi level two parent's class property used by the child class
# class Animal:
#     name1 = "lion"
# class Human:
#     name2 = "harsh"
# class Robots(Animal, Human):
#     name3 = "charli123"

# obj = Robots()
# print(obj.name3)
# print(obj.name1)

# # EX2
# class Factory:
#     def __init__(self, material, zips):
#         self.material = material
#         self.zips = zips

# class BhopalFactory(Factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color

# class Punefactory(BhopalFactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets



# Hierearchy Inheritance: In this type of inheritance, multiple child classes inherit from a single parent class.