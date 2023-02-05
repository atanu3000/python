import random
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
# 'A', 'B', 'C', 'D',
# 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
# 'V', 'W', 'X', 'Y', 'Z']

ascii_1 = ascii_2 =  0
string_dict = {}
name = []
def ascii(str):
    sum = 0
    for i in str:
        sum += ord(i)
    sum %= 100
    return sum

def hash(str, num):
    ascii_1 = ascii(str)
    while(num > 0):
        while True:
            new_str = []
            for i in str:
              new_str.append(random.choice(letter_list))
            if ascii(new_str) == ascii_1:
                names = " "
                for ch in new_str:
                    names += ch
                name.append(names)
                break
        num -= 1
    string_dict[ascii(str)] = name 
            

hash("atanu",5)
print(string_dict)