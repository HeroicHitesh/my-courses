# put your python code here
f_no = float(input())
s_no = float(input())
op = input()
if op == '+':
    print(f_no + s_no)
elif op == '-':
    print(f_no - s_no)
elif op == '*':
    print(f_no * s_no)
elif op == 'pow':
    print(f_no ** s_no)
elif op == '/':
    if s_no == 0:
        print('Division by 0!')
    else:
        print(f_no / s_no)
elif op == 'mod':
    if s_no == 0:
        print('Division by 0!')
    else:
        print(f_no % s_no)
elif op == 'div':
    if s_no == 0:
        print('Division by 0!')
    else:
        print(f_no // s_no)
