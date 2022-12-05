import collections

test_input = open('test_input.txt', 'r')
test_lines = test_input.readlines()

input_file = open('input.txt', 'r')
lines = input_file.readlines()


def parse_input(input):
    output = []
    input_lines = []
    for line in input:
        if line == "\n":
            break

        input_lines.append(line)

    numbers = input_lines[len(input_lines) - 1]
    split_numbers = numbers.split(" ")
    max_number = int(split_numbers[len(split_numbers) - 2])
    for i in range(max_number + 1):
        output.append(collections.deque())

    for i in reversed(input_lines):
        if i[1] == "1":
            continue

        index = 1
        counter = 1
        while True:
            if len(i) < counter:
                break
            if i[counter] != ' ':
                output[index].append(i[counter])

            index += 1
            counter += 4

    return output


def move(t, amount, from_tower, to_tower):
    for _ in range(amount):
        t[to_tower].append(t[from_tower].pop())


def new_move(t, amount, from_tower, to_tower):
    temp = []
    for _ in range(amount):
        temp.append(t[from_tower].pop())
    for i in reversed(temp):
        t[to_tower].append(i)


def find_output(t):
    out = ""
    for i in t:
        if len(i) == 0:
            out += ' '
        else:
            out += i.pop()
    print(out)


def part1(input):
    print("Part 1")

    t = parse_input(input)
    for line in input:
        # cheaty way to skip all the input lines
        if "move" not in line:
            continue

        # parse instructions
        instructions = line.split(" ")
        count = int(instructions[1])
        x = int(instructions[3])
        y = int(instructions[5])

        move(t, count, x, y)

    print(find_output(t))


def part2(input):
    print("Part 2")

    t = parse_input(input)
    for line in input:
        # cheaty way to skip all the input lines
        if "move" not in line:
            continue

        # parse instructions
        instructions = line.split(" ")
        count = int(instructions[1])
        x = int(instructions[3])
        y = int(instructions[5])

        new_move(t, count, x, y)

    print(find_output(t))


print("Tests")
part1(test_lines)
part2(test_lines)

print()

print("Real")
part1(lines)
part2(lines)
