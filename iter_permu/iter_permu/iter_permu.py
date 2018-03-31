from itertools import permutations
words, term = input().split()
li = list(permutations(sorted(words), int(term)))
new_li = []
for word in li:
    new_li.append("".join(word))
for l in new_li:
    print(l)
