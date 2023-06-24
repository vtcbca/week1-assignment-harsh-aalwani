#Write a python script to enter any number and print the sum of its digit.
total=0
n=int(input("Enter a number:"))
for i in range(1,n+1):
    total=total+i
print("Total =",total)
