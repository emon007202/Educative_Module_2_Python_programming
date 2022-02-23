# Problem statement#
# Implement the complete Student class by completing the tasks below
#
# Task#
# Implement the following properties as private:
#
# name
# rollNumber
# Include the following methods to get and set the private properties above:
#
# getName()
# setName()
# getRollNumber()
# setRollNumber()
# Implement this class according to the rules of encapsulation.
#
# Input#
# Checking all the properties and methods
#
# Output#
# Expecting perfectly defined fields and getter/setters

class Student:
    __name  =None
    __rollNumber = None
    def setName(self,x):
        self.__name = x


    def getName(self):
        return (self.__name)

    def setRollNumber(self,y):
        self.__rollNumber = y

    def getRollNumber(self):
        return (self.__rollNumber)

user = Student()
user.setName("Md. Emon")
user.setRollNumber("BT18GEC048")
print(user.getName())
print(user.getRollNumber())
