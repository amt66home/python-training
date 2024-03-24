class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class")

# To assign the above class(template) to an object you would do the following:
myobjectx = MyClass()

# Now the variable "myobjectx" holds an object of the class "MyClass" that contains 
# the variable and the function defined within the class called "MyClass".

# To access the variable inside of the newly created object "myobjectx" you would do the following:

myobjectx.variable

# So for instance the below would output the string "blah":

print(myobjectx.variable)

# You can create multiple different objects that are of the same class(have the 
# same variables and functions defined). However, each object contains independent 
# copies of the variables defined in the class. For instance, if we were to define 
# another object with the "MyClass" class and then change the string in the variable 
# above:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# To access a function inside of an object you use notation similar to accessing a variable:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class")

myobjectx = MyClass()
myobjectx.function()

# The __init__() function, is a special function that is called when the class is being initiated. 
# It's used for asigning values in a class.
class NumberHolder:

    def __init__(self, number):
        self.number = number

# Exercise
# We have a class defined for vehicles. 
# Create two new vehicles called car1 and car2. 
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van 
# named Jump worth $10,000.00.

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    colour = ""
    value = 100.0
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.colour,self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.colour = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.colour = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

# here is my example
class Cosmetic:
    name = ""
    kind = "Eye Makeup"
    colour = ""
    value = 10.0
    def description(self):
        desc_str = "%s is an %s, it's colour is %s and cost is £%.2f." %(self.name, self.kind, self.colour, self.value)
        return desc_str

lipstick = Cosmetic()
lipstick.name = "luscious lips"
lipstick.colour = "pink"
lipstick.value = 8.50

eyeshadow = Cosmetic()
eyeshadow.name = "smokey eyes"
eyeshadow.colour = "storm"
eyeshadow.value = 9.50

mascara = Cosmetic()
mascara.name = "flutter lashes"
mascara.colour = "black"
# mascara.value = 12.00

print(lipstick.description())
print(eyeshadow.description())
# no value set for mascara so class default used
print(mascara.description())


