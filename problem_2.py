# this function will help us to reverse our entered string
def string_Palindrome(s):
    return s == s[::-1]


s = input("enter the string to check palindrome:")
# here we pass our entered sting in a function we have created
ans = string_Palindrome(s)

if ans:
    print("string is palindrome")
else:
    print("string is not palindrome")
