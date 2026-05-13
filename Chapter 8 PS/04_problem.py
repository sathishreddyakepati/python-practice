# 4. Write a recursive function to calculate the sum of first n natural numbers. 


def sumN(n):
    if n==1:
        return 1
    else:
         return n + sumN(n-1)

a = int(input("Enter the number(n): "))
ans = sumN(a)
print(ans)