from collections import OrderedDict

words = OrderedDict()
for _ in range(int(input())):
    word = input()
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
for each in words.keys():
    print(words[each], end = ' ')
