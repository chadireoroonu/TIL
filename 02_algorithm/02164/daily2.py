from itertools import permutations
from pprint import pprint
a = range(1, 5)
b = list(permutations(a))
for i in b:
    pprint(i)
print()
c = list(combinations(a, 3))
for i in c:
    print(i)