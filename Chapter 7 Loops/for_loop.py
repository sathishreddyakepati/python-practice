# The range() function in python is used to generate a sequence of number. 

for i in range(4):
    print(i)

    '''
    output
    1
    2
    3
    4
    '''
# FOR LOOP WITH ELSE

#Break -‘break’ is used to come out of the loop when encountered. 
# It instructs the program to – exit the loop now. 
print("---Break Statement---")
s = [7,8,5,9,0,23]

for i in s:
    if i ==5:
        break
    print(i)



# ‘continue’ is used to stop the current iteration of the loop and continue with the next 
# one. It instructs the Program to “skip this iteration”.
print("---Continue Statement---")
s = [1,5,6,7]

for i in s:
    if i ==5:
        continue
    print(i)


#pass is a null statement in python. 
# It instructs to “do nothing”.

l =[1,7,8]
for item in l:
    pass