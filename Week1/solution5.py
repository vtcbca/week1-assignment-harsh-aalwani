#Write a python script to enter any string and count vowel.
n=0
str1=input("Write a string: ")
for i in str1:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        n=n+1
print("The number of vowels in string: ",n)
