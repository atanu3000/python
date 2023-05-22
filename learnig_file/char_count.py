# str = 'the quick brown fox jumps over the lazy dog'
str = input("Enter your string: ")
str = str.replace(' ', '')

import string
# d = dict.fromkeys(string.ascii_lowercase, 0)  # using fromkeys()
d = {alpha : 0 for alpha in string.ascii_lowercase}    # using comprehension method

for alpha in str:
    d[f'{alpha}'] += 1

# for key, val in d.items():
#     if val != 0:
#         print(f'{key} : {val}')

print({f'{key} : {val}' for key, val in d.items() if val != 0})

# print({x for x in range(10)})