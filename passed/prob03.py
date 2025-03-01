with open("input.txt","r") as file:
    lines = file.readlines()

if len(lines) - 1 == 1:
    print("Hey, ChatGPT, I need a code!")
else:
    print("Hey, ChatGPT, I need "+str(len(lines) -1)+" codes!")

    