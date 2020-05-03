scores = input().split()
# put your python code here
correct = 0
incorrect = 0
for i in range(len(scores)):
    if scores[i] == 'C':
        correct += 1
        if i == len(scores) - 1:
            print('You won')
            break
    if scores[i] == 'I':
        incorrect += 1
        if incorrect == 3:
            print('Game over')
            break
print(correct)
