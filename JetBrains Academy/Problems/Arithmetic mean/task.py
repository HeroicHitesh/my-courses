numbers = [int(x) for x in input().split()]
sum_no = 0
for i in numbers:
    sum_no += i
print(sum_no / len(numbers))
