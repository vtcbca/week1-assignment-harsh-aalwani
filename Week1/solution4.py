'''
Write a python script to enter any number, if it is integer number, then check its armstrong or not.
Print appropriate message if it is not palindrome.
'''
n=float(input("Enter a number:"))
if int(n)==n:
    temp = int(n)
    add_sum = 0
    while temp != 0:
        m = temp % 10
        add_sum += m*m*m
        temp = temp//10
    if add_sum == int(n):
        print('The number is Integer and Armstrong Number')
    else:
        print('The number is Integer and not an Armstrong Number')
else:
    print("The number is not integer.")
