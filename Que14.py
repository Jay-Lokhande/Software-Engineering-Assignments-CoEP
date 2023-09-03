num = int(input("Enter the num: "))

def fact(num):
    if num == 0: return 1
    return fact(num-1)*num

print(fact(num))