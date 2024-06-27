def grey_code_subsets(n):
    for i in range(1 << n):
        grey = i ^ (i >> 1)
        subset = []
        for j in range(n):
            if grey & (1 << j):
                subset.append(j + 1)
        yield subset

n = 3
print(f"Wyniki dla n = {n}:")

for res in grey_code_subsets(n):
    print(res)
