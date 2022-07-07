# this is list that we are going to find the runner up and maximum
num_list= [5, 8, 2, 6, 8, 5, 8, 7,10]
# this value will help us in if condition
a = 0
b = 0
maximun = num_list[0] # this maxim value to store the first element in list
for i in num_list:
   if i > a:
      a, b = i,a
   elif a > i > b:
      b = i
   if maximun<i:
      maximun=i

print("the runner up is",b)
print("the maximum is:",maximun)
