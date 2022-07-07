# definition of class pernson
class Person:
    My_full_name = "Nsabimana Albert" # this is argument of person class
    def greet(self): # greet method that will help to display the names
        print("Hi! Dear My name is ", self.My_full_name,"welcome!")
# this is the  instantiation of object
fullnames1 = Person()
# Accessing class fields/method using our created object
fullnames1.greet()