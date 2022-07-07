# this the list l which contain the character of word stored in string s
l=['g','o','o','g','l','e']
s= "google"  # string
dict = {} # this dictionary that help to store the character
for i in l:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

print (dict)
