# # string = input()
# # bad_chars = [',', '.', '!', '?']
# # for i in bad_chars:
# #     string = string.replace(i, '')
# # print(string.lower())

import re
p = re.compile(r"[!,.?]")
print(p.sub("", input().lower()))

# text = input()
# marks = ".,!?"
#
# for mark in marks:
#     if mark in text:
#         text = text.replace(mark, "")
# print(text.lower())
