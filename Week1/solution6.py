#Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
str0=input("Write a string: ")
str1=input("Enter start character: ")
str2=input("Enter end character: ")
x = str0.index(str1)
y = str0.index(str2)
print("Part of string: ",str0[x:y+1])
