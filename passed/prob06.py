with open("input.txt","r") as file:
    area = float(file.readline().rstrip())

l = []

for i in range(int(area/2) + 2):
    if area % (i+2) == 0:
        l.append(str(i+2)+" x "+str(int(area/(i+2))))

l.reverse()


for i in range(len(l)):
    if i < len(l)/2:
        print(l[i])
