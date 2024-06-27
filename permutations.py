def permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for i in range(len(elements)):
            for perm in permutations(elements[:i] + elements[i+1:]):
                yield [elements[i]] + perm

n = [1, 2, 3]
print(f"Wyniki dla n = {n}:")

for res in permutations(n):
    print(res)
