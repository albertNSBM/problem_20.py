# this list to check the from every number divisible by three
num_list = [5, 6, 9, 10, 15, 17, 18, 21,60,30,20]
# this is variable that will count the number
count = 0
for i in num_list:
    if i % 3 == 0:
        count = count + 1
print(count,"of the this list is divisible by 3  ")
