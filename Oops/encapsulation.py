class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def celebrate_birthday(self):
        self.__age += 1

# Creating an instance of Person
john = Person("John", 30)

# Accessing attributes using getter methods
print("Name:", john.get_name())
print("Age:", john.get_age())

# Trying to modify the age directly (not allowed)
#john.__age += 1  # This will raise an AttributeError

# Celebrating birthday using a method
john.celebrate_birthday()
print("New Age after Birthday Celebration:", john.get_age())
