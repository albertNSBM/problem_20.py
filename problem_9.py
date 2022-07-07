# dictionary  that will  help us to  store the binary digit entered
num_list = []
num = [x for x in input().split(',')]# the function that help to split the entered digit
for p in num:
    x = int(p,2)
    if not x%5:
       num_list.append(p)
print(','.join(num_list))