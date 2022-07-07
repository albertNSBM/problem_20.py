# this is the list to find the maximum number and minimum using for loop
num_list = [2, 4, 5, 6, 7, 23, 60, 70, 200, 435, 1]
# this variable will help to store largest number
largest = num_list[0]
for i in num_list:
    if i > largest:
        largest = i
print("the largest is:")
print(largest)
# this variable will help to store smallest number
smallest = num_list[0]
for i in num_list:
    if i < smallest:
        smallest = i
print("the smallest is:")
print(smallest)
