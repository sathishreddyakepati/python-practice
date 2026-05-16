# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.
def table(n):
        table=""
        for j in range(1,11):     
                table = table+f"{n} x {j} = {n*j}\n"
        
        with open(f"Tables/table_{n}.txt","w") as f:
                f.write(table)

        

for k in range(2,21):
        table(k)
    