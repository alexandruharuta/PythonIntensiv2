print('Insert two numbers')
while True:
    a = int(input())
    b = int(input())
    if (a > -1) and (b > -1):
        print(a)
        print(a + b)
        print(a - b)
        break
    elif (a < 0) or (b < 0):
        print("Numbers are not positive")