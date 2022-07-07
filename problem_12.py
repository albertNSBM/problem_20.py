# program to find the number appear in list1 but not in list2
def getlist():
    # two lists to be entered from the user
    num_list1=[]
    num_list2=[]
    n=int(input("enter number of  list1 elements:"))
    for i in range(n):
        o=int (input("enter the element{}:".format(i+1)))
        num_list1.append(o)
    print("list one=",num_list1)
    n=int(input("enter number of  list2 elements:"))
    for i in range(n):
        o=int (input("enter the element{}:".format(i+1)))
        num_list2.append(o)
    print("list two=",num_list2)
    # builtin function difference() hel to find difference using sets
    difference_1 = set(num_list1).difference(set(num_list2))
    print("the number in list1 not in list2",difference_1)
getlist() # function call