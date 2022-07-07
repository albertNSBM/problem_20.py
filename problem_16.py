# class to that contain two methods
class program():
    def __init__(self):
        self.str1 = ""

    # function to accept string from the user
    def get_String(self):
        self.str1 = input("enter the string:")

    # function to print the string accepted
    def print_String(self):
        print(self.str1.upper())


str1 = program()  # object instantiation
str1.get_String()  # accessing class method
str1.print_String()  # accessing class method
