with open("input.txt","r") as file:
    line = file.readline().rstrip()

l = line.split(" ")

out = ""

for word in l:
    out += word[0]

print(out)