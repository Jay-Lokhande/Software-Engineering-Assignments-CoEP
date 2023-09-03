numOne = float(input("Enter First Number: "))
numTwo = float(input("Enter Second Number: "))
operator = input("Enter the Operator: ")
ans = 0
if (operator == "+"):
    ans = numOne + numTwo
elif (operator == "-"):
    ans = numOne - numTwo
elif (operator == "/"):
    ans = numOne / numTwo
elif (operator == "*"):
    ans = numOne * numTwo
print(ans)