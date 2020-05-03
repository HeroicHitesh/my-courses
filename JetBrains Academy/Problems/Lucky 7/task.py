n = int(input())
while n > 0:
    mul = abs(int(input()))
    if mul % 7 == 0:
        print(mul ** 2)
    n -= 1
