from itertools import product
A = map(int, input().split())
B = map(int, input().split())
ListA = []
ListB = []
for i in A:
    ListA.append(i)
for i in B:
    ListB.append(i)
if len(ListA) > 0 and len(ListA) < 30 and len(ListB) > 0 and len(ListB) < 30:
    for item in product(ListA,ListB):
        print(item,end=' ')
else:
    exit