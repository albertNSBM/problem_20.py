# this is our range from 2000 to 3200
a = int(2000)
b = int(3200)

# check until end of the range is achieved
while a <= b:

    # check if number is divisible by 7 and not multiple of 5
    if a % 7 == 0 and a % 5 != 0:
        print(a,"," )
    a += 1
