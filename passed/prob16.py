with open("input.txt") as file:
    inpt = file.readlines()
    d = float(inpt[0].split(" ")[0])
    units = inpt[0].split(" ")[1].rstrip()
    time = float(inpt[1].rstrip())

if units == "m":
    d = d * 39.37008 / 12 / 5280
if units == "in":
    d = d / 12 / 5280
if units == "ft":
    d = d /5280
if units == "y":
    d = d * 3 / 5280

time = time / 60 / 60

mph = d/time
mph = str(mph)
mph = mph[0:mph.index(".")+3]

print(mph + " miles/hour")
