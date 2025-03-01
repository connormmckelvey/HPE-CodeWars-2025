with open("input.txt","r") as file:
    line = file.readline().rstrip()

nums = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
}

for char in line:
    nums.update({char:nums.get(char) + 1})

low = nums.values()[0]
c = 0
for i in range(len(nums.values())):
    if nums.values[i] < low:
        low = nums.values[i]
        c = nums.keys[i]

print(str(nums.keys()[c])+": "+str(low))


    