import random

#t his is function to shiffle the list
def randomly_shiffle():
    num_list = [1, 4, 5, 6, 3, 6, 7, 2, 7, 9, 40, 56]
    print("before shiffle the list:", num_list)

    # this is builtin function that shiffle the list randomly
    random.shuffle(num_list)
    print("after shiffle the list:", num_list)
#function call
randomly_shiffle()
