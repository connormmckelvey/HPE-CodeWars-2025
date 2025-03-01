with open("input.txt","r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    
def isVowel(s):
    vowels = ["a","i","e","o","u"]
    if s in vowels:
        return True
    else:
        return False

line_list = []

for line in lines:
    l = []
    for char in line:
        l.append(char)
    line_list.append(l)

vowel_pairs = {

}

for line in line_list:
    for i in range(len(line)):
        if i == 0:
            if isVowel(line[i]) and isVowel(line[i+1]) and isVowel(line[i+2]) == False:
                if line[i] + line[i+1] in vowel_pairs.keys():
                    vowel_pairs.update({line[i] + line[i+1]:vowel_pairs.get(line[i] + line[i+1]) + 1})
                else:
                    vowel_pairs.update({line[i] + line[i+1]:1})
        elif i + 2 == len(line):
            if isVowel(line[i]) and isVowel(line[i+1]):
                if line[i] + line[i+1] in vowel_pairs.keys():
                    vowel_pairs.update({line[i] + line[i+1]:vowel_pairs.get(line[i] + line[i+1]) + 1})
                else:
                    vowel_pairs.update({line[i] + line[i+1]:1})

        elif i + 2 > len(line):
            pass
        else:
            if isVowel(line[i]) and isVowel(line[i+1]) and isVowel(line[i+2]) == False and isVowel(line[i-1]) == False:
                if line[i] + line[i+1] in vowel_pairs.keys():
                    vowel_pairs.update({line[i] + line[i+1]:vowel_pairs.get(line[i] + line[i+1]) + 1})
                else:
                    vowel_pairs.update({line[i] + line[i+1]:1})

for key in vowel_pairs:
    print(key +": "+str(vowel_pairs[key]))