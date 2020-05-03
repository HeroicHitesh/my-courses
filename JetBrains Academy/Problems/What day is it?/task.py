# # offset = (input())
# # if offset == '-12':
# #     print('Monday')
# # elif offset == '-11':
# #     print('Monday')
# # elif offset == '-10':
# #     print('Tuesday')
# # elif offset == '-9':
# #     print('Tuesday')
# # elif offset == '-8':
# #     print('Tuesday')
# # elif offset == '-7':
# #     print('Tuesday')
# # elif offset == '-6':
# #     print('Tuesday')
# # elif offset == '-5':
# #     print('Tuesday')
# # elif offset == '-4':
# #     print('Tuesday')
# # elif offset == '-3':
# #     print('Tuesday')
# # elif offset == '-2':
# #     print('Tuesday')
# # elif offset == '-1':
# #     print('Tuesday')
# # elif offset == '0':
# #     print('Tuesday')
# # elif offset == '+1':
# #     print('Tuesday')
# # elif offset == '+2':
# #     print('Tuesday')
# # elif offset == '+3':
# #     print('Tuesday')
# # elif offset == '+4':
# #     print('Tuesday')
# # elif offset == '+5':
# #     print('Tuesday')
# # elif offset == '+6':
# #     print('Tuesday')
# # elif offset == '+7':
# #     print('Tuesday')
# # elif offset == '+8':
# #     print('Tuesday')
# # elif offset == '+9':
# #     print('Tuesday')
# # elif offset == '+10':
# #     print('Tuesday')
# # elif offset == '+11':
# #     print('Tuesday')
# # elif offset == '+12':
# #     print('Tuesday')
# # elif offset == '+13':
# #     print('Tuesday')
# # elif offset == '+14':
# #     print('Wednesday')
#
#
# offset = int(input())
# if offset < -10:
#     print('Monday')
# elif offset < 14:
#     print('Tuesday')
# else:
#     print('Wednesday')


offset = int(input())

weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

hour = 10.5
diff = hour + offset + 24

weekday = int(diff // 24 % 7)

print(weekdays[weekday])
