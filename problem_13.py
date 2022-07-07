# program to find the intersection between two lists
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
    # builtin function intersection() to find intersection in a sets
    intersection_1 = set(num_list1).intersection(set(num_list2))
    print("the intersection are:",intersection_1)
getlist() # function call