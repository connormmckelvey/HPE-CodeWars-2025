with open("input.txt","r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        

amt_of_dec = int(lines[0])
lines.remove(str(amt_of_dec))
nums = []


for line in lines:
    if line == "000":
        break
    else:
        if len(line) - 1 - line.index(".") > amt_of_dec:
            n = line[0:line.index(".") + amt_of_dec + 1]
        else:
            n = line
        nums.append(float(n))

for n in nums:
    print(n)