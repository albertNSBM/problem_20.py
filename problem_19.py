# ATM service  implementation program
def withdraw(num1, num2): # this is withdraw method
    return num1 - num2
def deposite(num1, num2): # This is deposite method
    return num1 + num2

def balance(num1, num2): #  current balance method
    return num1 + num2

def divide(num1, num2):
    return num1 / num2


print("CHOOSE A SERVICE:")
print("1.WITHDRAW")
print("2.DEPOSITE")
print("3.CURRENT BALANCE")
print("4.EXIT")

while True:
    # takes input from the user
    choice = input("Choose one choice from those ones (1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        current_balance = 2000000
        #money = float(input("Enter amount: "))

        if choice == '1':
            money = float(input("Enter amount: "))
            print(" you have withdrawn", money, "from", current_balance, "new balance", withdraw(current_balance, money),"thank you!")

        elif choice == '2':
            money = float(input("Enter amount: "))
            print("you have deposited", money, "to", current_balance, "new balance", deposite(current_balance, money))

        elif choice == '3':
            money = float(input("Enter amount: "))
            print(" your balance is now:", balance(current_balance, money))

        elif choice == '4':
            go_out = input("ENTER EXIT IF YOU WANT TO EXIT: ")
            if go_out == "exit" or go_out=="EXIT":
                break

        else:
            print("WRONG INPUT")
