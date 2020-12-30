class MyClass:
    name = "Raghav"

    def __init__(self, name, age):    #  The __init__ function is used to initialize a class. It is similar to a Java Constructor.
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a+b)

x = MyClass("John", 40)                # An object called x is created from the class called MyClass. There are two parameters John and 40
print(x.name)
x.sum(4, 5)
del x.name
print(x.age)



