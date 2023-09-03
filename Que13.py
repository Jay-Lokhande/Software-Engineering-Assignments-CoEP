string = "abccwba"
checkSring = ""
for i in range(len(string)-1, -1, -1):
    checkSring += string[i]
if(string == checkSring):
    print(True)
else:
    print(False)