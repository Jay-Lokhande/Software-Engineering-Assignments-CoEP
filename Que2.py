print("Check Number is Prime or not")

flag = True
while flag:
    num = int(input("Enter the Number: "))

    if num <= 0:
        print("Number cannot be negative or zero")
    else:
        arr = []
        counter = 0
        for i in range(1, num + 1):
            if num % i == 0:
                counter += 1
                arr.append(i)

        if num == 1 or counter == 2:
            print(f'It is a Prime Number \n& Divisors of {num} are')
            print(arr)
        else:
            print(f'Number is not Prime Number \n& Divisors of {num} are')
            print(arr)

    opp = input("Press N to check another Number Press E to exit: ")
    if opp == "E":
        flag = False
