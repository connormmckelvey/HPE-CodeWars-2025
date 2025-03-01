with open("input.txt","r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    lines.pop(-1)

emails = []

for line in lines:
    l = line.split(",")
    for x in l:
        x = x.split(" ")
        for e in x:
            if e.casefold() in emails:
                pass
            else:
                emails.append(e.casefold())

emails.sort()

for e in emails:
    print(e+";")

