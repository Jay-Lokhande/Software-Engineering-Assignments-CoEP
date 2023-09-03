numOne = float(input("Enter First Number: "))
numTwo = float(input("Enter Second Number: "))
numThree = float(input("Enter Third Number: "))

maxOne = numOne if numTwo < numOne else numTwo
maxTwo = numThree if maxOne < numThree else maxOne
print(maxTwo)