#1. Write a program to find the greatest of four numbers entered by the user. 
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
max = a
if(b>max):
    max = b

if(c>max):
    max = c

if(d>max):
    max = d

print("Greatest numbers is ",max)