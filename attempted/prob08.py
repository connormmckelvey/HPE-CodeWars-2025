with open("input.txt","r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

key = lines[1]
word = lines[0]

num = word.lower().count(key.lower())

print("There are "+str(num)+" "+key+"'s in "+word)