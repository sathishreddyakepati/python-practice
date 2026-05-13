# 7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3
# n = int(input("Enter the number: "))
# i = 1

# while(i<=n):
#     k = 1
#     j = 2*i-1
#     while(k<=j):
#         print("*",end="")
#         k = k+1
#     print()
#     i+=1

n = int(input("Enter the number(n): "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()
