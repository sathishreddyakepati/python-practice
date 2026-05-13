# 6. Write a python function which converts inches to cms. 

def InchToCm(n):
    cm = n*2.54
    print(f"{n} Inches = {cm} cms")


a = int(input("Enter length in inches: "))
InchToCm(a)