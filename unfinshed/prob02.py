with open("input.txt") as file:
    l = []
    line = file.readline().rstrip()
    for x in line:
        l.append(x)


length = len(l)
removed = []
for i in range(length):
    if (i + 1) % 3 == 0:
        print(l[i])
        re = l.pop(i)
        removed.append(re)

out1 = ""
out2 = ""
for ch in l:
    out1 += ch
for ch in removed:
    out2 += ch

print(out1)
print(out2)