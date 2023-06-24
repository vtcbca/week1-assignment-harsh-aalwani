#Write a python script to enter any number and print the sum of its digit.
total=0
n=input("Enter a number:")
for i in n:
    total=total+int(i)
print("Total =",total)
