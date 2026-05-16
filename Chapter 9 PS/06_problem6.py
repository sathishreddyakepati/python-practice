# 6. Write a program to mine a log file and find out whether it contains ‘python’. 
word = "python"

f = open("log.txt","r")
line = f.readline()
i = 1
while(line != ""):
    if(word in line):
        print(f"yes,{word} is present in line no:{i}")
        break
    else:
        line = f.readline()
        i+=1

if(line==""):
        print(f"No,{word} is not present in this file")
f.close()