lst = []
while 1:
    n = input()
    if n == '.':
        print(min(lst))
        break
    lst.append(float(n))
