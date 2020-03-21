# Day 4
"""
Name: 
    Vowels Finder
Filename: 
    vowels.py
Problem Statement:
    Remove all the vowels from the list of states  
Hint: 
    Use nested for loops and while
Sample Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
Sample Output:
    ['lbm', 'clfrn', 'klhm', 'flrd'] 
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']

def vowel_removal(state):
    vowels = ('a','e','i','o','u')
    for s in state:
        if s in vowels:
            state = state.replace(s,'')
    return state

print(list(map(vowel_removal, list(map(lambda x:x.lower(), state_name)))))