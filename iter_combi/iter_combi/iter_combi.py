from itertools import combinations
words, term = input().split()
new_li = []
for i in range(int(term)):
    li = list(combinations(sorted(words), i+1))
    for word in li:
        new_li.append("".join(word))
for l in new_li:
    print(l)

