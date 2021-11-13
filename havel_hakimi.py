n = str(input("Give me a permutation, please: "))
perm = []
perm1 = []
for i in n:
    perm.append(int(i))
for i in range(len(n)):
    count = 0
    for j in range(i+1, len(n)):
        if perm[i] > perm[j]:
            count += 1
    perm1.append(count)
print("Here is the sequence: ")
for i in range(len(perm1)):
    print(perm1[i], end=", ")
