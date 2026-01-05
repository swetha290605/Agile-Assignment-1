# Code-Project-1
#this is a multiplication table
n=input("Enter a number: ")
n= int(n) #converted to integer
for i in range(1,11):
    mul=n*i #calculation procedure
    print("----displaying table-----")
    print(f"{n}*{i}= ", mul) #correctly formated Print Statement