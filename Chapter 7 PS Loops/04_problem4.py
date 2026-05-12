# 4. Write a program to find whether a given number is prime or not. 
n = int(input("Enter number: "))
x = int(n**0.5)

if n<=1:
    print(n," is not a prime number.")
i = 2
while(i<=x):
    if n%i == 0:
        print(n," is not a prime number.")
        break
    i+=1
    
if(i>x):
    print(n," is a prime number.")
