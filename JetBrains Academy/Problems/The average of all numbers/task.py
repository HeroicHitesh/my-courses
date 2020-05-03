# put your python code here
a = int(input())
b = int(input())
sum_i = 0
count_i = 0
for i in range(a, b+1):
    if i % 3 == 0:
        sum_i += i
        count_i += 1
print(sum_i / count_i)
