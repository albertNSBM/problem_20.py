# the program to check the number of times character comes in a string
s=("goodmorning")
count=0
num=s[0]
# loop help for checking into the string
for i in s:
    if i==num:
        count=count+1
        
print(num,"is in string",count,"times")