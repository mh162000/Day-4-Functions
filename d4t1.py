num = int(input("Insert a number: "))

def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

table(num)