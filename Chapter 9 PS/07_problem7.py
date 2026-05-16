# 7. Write a program to find out the line number where python is present from ques 6. 
word = "python"

with open("log.txt") as f:
    data = f.read()

if(word in data):
    print(f"Yes,{word} is present in log file")
else:
    print(f"No,{word} is not present in log file")