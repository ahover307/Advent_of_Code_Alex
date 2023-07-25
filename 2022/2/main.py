input_file = open('input.txt', 'r')
lines = input_file.readlines()

win = 6
loss = 0
tie = 3

rock = 1
paper = 2
scissors = 3


def wins(me, them):
    if them == "A":
        if me == "X":
            return tie
        elif me == "Y":
            return win
        elif me == "Z":
            return loss
    elif them == "B":
        if me == "X":
            return loss
        elif me == "Y":
            return tie
        elif me == "Z":
            return win
    elif them == "C":
        if me == "X":
            return win
        elif me == "Y":
            return loss
        elif me == "Z":
            return tie


# Part 1
print("Part 1")

score = 0
for line in lines:
    them = line[0]
    me = line[2]

    if me == "X":
        score += rock
    elif me == "Y":
        score += paper
    elif me == "Z":
        score += scissors

    score += wins(me, them)

print(score)

print()
# Part 2
print("Part 2")
score = 0
for line in lines:
    them = line[0]
    con = line[2]

    # we need to lose
    if con == "X":
        score += 0
        if them == "A":
            score += scissors
        if them == "B":
            score += rock
        if them == "C":
            score += paper
    # Tie
    if con == "Y":
        score += 3
        if them == "A":
            score += rock
        if them == "B":
            score += paper
        if them == "C":
            score += scissors
    # Win
    if con == "Z":
        score += 6
        if them == "A":
            score += paper
        if them == "B":
            score += scissors
        if them == "C":
            score += rock

print(score)
