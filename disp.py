# this is a multiplication table
n = int(input("Enter a number: "))

print("----displaying table-----")
for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")
