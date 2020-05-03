col = int(input())
row = int(input())
if (row == 1 and (col == 1 or col == 8)) or (row == 8 and (col == 1 or col == 8)):
    print(3)
elif ((row == 1 or row == 8) and 1 < col < 8) or ((col == 1 or col == 8) and 1 < row < 8):
    print(5)
else:
    print(8)
