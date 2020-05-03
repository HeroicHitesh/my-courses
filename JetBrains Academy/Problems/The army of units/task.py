no_of_units = int(input())
if no_of_units < 1:
    print('no army')
elif no_of_units <= 9:
    print('few')
elif no_of_units <= 49:
    print('pack')
elif no_of_units <= 499:
    print('horde')
elif no_of_units <= 999:
    print('swarm')
else:
    print('legion')
