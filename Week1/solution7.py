#Write a python script to enter any string, replace vowel with its position number.
str1=input("Write a string: ")
str0=str1
res=str1
for i in str1:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        x = str1.index(i)
        str1 = str1[:x] + str(x) + str1[x+1:]
print("Old string: ",str0)
print("New string: ",str1)
