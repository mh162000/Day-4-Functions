num = int(input("Insert a number "))
def check_even(num):
    if num % 2 == 0:
        print ("Even")
    else:
        print("Odd")
    check_even(num)
  