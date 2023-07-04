'''
Write a python script to enter any number,if it is integer number, then check its palindrom or not.
Print appropriate message if it is not palindrome.
'''
n=float(input("Enter a number:"))
if int(n)==n:
    m=temp=int(n)
    rev=0
    while(m>0):
        dig=m%10
        rev=rev*10+dig
        m=m//10
    if(temp==rev):
        print("The number is integer and palindrome.")
    else:
        print("The number is integer and not a palindrome.")
else:
    print("The number is not integer.")
