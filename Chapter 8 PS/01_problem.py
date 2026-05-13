# 1. Write a program using functions to find greatest of three numbers. 

def maxi(a,b,c):
    max = a
    if b<max:
        max = b
    if c>max:
        max = c

    print(f"Maximum of {a},{b} and {c} is {max}.")

maxi(4,-5,7)