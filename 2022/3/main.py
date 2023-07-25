input_file = open('input.txt', 'r')
lines = input_file.readlines()

def priority(item):
    if str(item).islower():
        return ord(item) - 96
    else:
        return ord(item) - 65 + 27


# Part 1
print("Part 1")

score = 0
for line in lines:
    map = []
    a = line[:len(line)//2]
    b = line[len(line)//2:]

    for letter in a:
        if letter in b and letter not in map:
            map.append(letter)
            score += priority(letter)

print(score)

print()
# Part 2
print("Part 2")


score = 0
a = ""
b = ""
c = ""
def calc():
    for letter in a:
            if letter in b and letter in c and letter != '\n':
                map.append(letter)
                return priority(letter)

for line in lines:
    if a == "":
        a = line
        continue
    elif b == "":
        b = line
        continue
    elif c == "":
        c = line
        continue
    else:
        score += calc()

        # on this iteration of the loop we already grabbed the next line, make sure we keep it
        a = line
        b = ""
        c = ""

# it stops the loop on the last iteration before we are actually done
score += calc()
print(score)
