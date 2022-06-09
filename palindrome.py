def Palindrome(str):
       
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

string=input("Enter a string : ")
ans = Palindrome(string)
 
if (ans):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")