with open("input.txt") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    lines.pop(-1)

for line in lines:
    print(line.swapcase())

#array of array of chars
l = []

for i in range(len(lines)):
    linelist = []
    lines[i] = lines[i].rstrip()
    for ch in lines[i]:
        linelist.append(ch)
    l.append(linelist)

#for line in l:
#    for ch in line:
#        if ch.isLower():
#            ch = ch.upper()
#        else:
#            ch = ch.casefold()
            