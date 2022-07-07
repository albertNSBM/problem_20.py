# function to calculate the double of entered number/numbers
def get_double(p):
    return 2 * p

# This list will store the all element from user either duplicate or non-duplicate
user_number = []
# This input m will be used in range of loop
m = int(input(" How many numbers you want to enter??!: "))
for n in range( m ):
    Elements = int(input("Enter number:"))
    user_number.append(Elements)

# this  function contain the condition to check if the number has bees seen or not
def check_numbers(x):
    # dictionary tha will help to store the entered number as key and result as value
    Dictionary = {}
    # This is a list to store the non-duplicate element from user
    List_nonduplicate = []
    for i in x:
        if i not in List_nonduplicate:  # condition to check if number is not in list and add it
            List_nonduplicate.append(i)
    for i in List_nonduplicate:
        Dictionary.update({i: (get_double(i))})  # to update dictionary by adding the value from function
    return Dictionary

print(check_numbers(user_number))
