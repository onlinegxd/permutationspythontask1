from itertools import permutations
val = input("Enter symbols\n")
print([''.join(p) for p in permutations(val)])
