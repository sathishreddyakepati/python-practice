# 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * * 

n = int(input("Enter the number(n): "))

for i in range(1,n+1):
    if (i==1 or i==n):
        for j in range(1,n+1):
            print("*",end="")
    else: 
        print("*",end="")
        for k in range(2,n):
            print(" ",end="")
        print("*",end="")
    print()
    


                     
      
