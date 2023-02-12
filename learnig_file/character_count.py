from collections import Counter


text = "Good morning friend. Have a nice day."
# text = text.split()
text = text.replace(" ", "").replace(".", "")
text = text.lower()
text = sorted(text)
print(len(text))

res = {}
l = len(text)
ind = 0

for i in text:
    count = 0
    for j in text:
        ind += 1
        if i == j:
            count += 1
            res[i] = count
print(res)
print(ind)

