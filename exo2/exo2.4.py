a = 0
b = 10

while b != 0:
    b -= 1
    if b % 2 == 1:
        print("b=", b)
    while a < b:
        a += 1
        print("a=", a)
        break