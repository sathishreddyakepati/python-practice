# 10. Write a program to print multiplication table of n using for loops in reversed 
# order. 

n = int(input("Enter the number: "))

i = 10
while(i>0):
    print(n," x ",i," = ",n*i)
    i-=1
