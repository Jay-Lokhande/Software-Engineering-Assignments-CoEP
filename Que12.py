count = 0
year = 2000
flag = True
while(flag):
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        count += 1
        print(year)
    year += 1
    if (count == 10):
        flag = False