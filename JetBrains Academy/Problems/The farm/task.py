money = int(input())
cost_of_chicken = 23
cost_of_goat = 678
cost_of_pig = 1296
cost_of_cow = 3848
cost_of_sheep = 6769
no_of_chicken = money // 23
no_of_goat = money // 678
no_of_pig = money // 1296
no_of_cow = money // 3848
no_of_sheep = money // 6769
if no_of_sheep > 0:
    if no_of_sheep > 1:
        print(str(no_of_sheep) + ' sheep')
    else:
        print(str(no_of_sheep) + ' sheep')
elif no_of_cow > 0:
    if no_of_cow > 1:
        print(str(no_of_cow) + ' cows')
    else:
        print(str(no_of_cow) + ' cow')
elif no_of_pig > 0:
    if no_of_pig > 1:
        print(str(no_of_pig) + ' pigs')
    else:
        print(str(no_of_pig) + ' pig')
elif no_of_goat > 0:
    if no_of_goat > 1:
        print(str(no_of_goat) + ' goats')
    else:
        print(str(no_of_goat) + ' goat')
elif no_of_chicken > 0:
    if no_of_chicken > 1:
        print(str(no_of_chicken) + ' chickens')
    else:
        print(str(no_of_chicken) + ' chicken')
else:
    print('None')
