with open("input.txt") as file:
    lines = file.readlines()

name = lines[0].split(" ")[0]
amt_of_vend = int(lines[0].split(" ")[1].rstrip())

amt_shirt = 0
amt_stick = 0
amt_hat = 0

for line in lines:
    if line == lines[0]:
        pass
    else:
        ns = line.split(" ")
        amt_shirt += int(ns[0])
        amt_hat += int(ns[1])
        amt_stick += int(ns[2])

total_amt = amt_shirt * 13 + amt_stick * 2 + amt_hat * 9
ssh = str(amt_shirt) + " shirt"
sst = str(amt_stick) + " sticker"
sha = str(amt_hat) + " hat"

if amt_shirt != 1:
    ssh += "s"
if amt_stick != 1:
    sst += "s"
if amt_hat != 1:
    sha += "s"

print(name + " spend $"+str(total_amt) + " on "+ssh+", "+sha+", and "+sst+".")

