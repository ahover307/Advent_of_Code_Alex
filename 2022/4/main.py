test_input = open('test_input.txt', 'r')
test_lines = test_input.readlines()

input_file = open('input.txt', 'r')
lines = input_file.readlines()


def part1(input):
    print("Part 1")
    score = 0
    for line in input:
        a, b = line.split(',')
        a_left, a_right = a.split('-')
        b_left, b_right = b.split('-')
        x = set()
        y = set()
        for i in range(int(a_left), int(a_right) + 1):
            x.add(i)

        for i in range(int(b_left), int(b_right) + 1):
            y.add(i)

        if x.issubset(y) or y.issubset(x):
            score += 1

    print(score)


def part2(input):
    print("Part 2")
    score = 0
    for line in input:
        a, b = line.split(',')
        a_left, a_right = a.split('-')
        b_left, b_right = b.split('-')
        x = set()
        y = set()
        for i in range(int(a_left), int(a_right) + 1):
            x.add(i)

        for i in range(int(b_left), int(b_right) + 1):
            y.add(i)

        if x.intersection(y) or y.intersection(x):
            score += 1

    print(score)
print("Tests")
part1(test_lines)
part2(test_lines)
print()
print("Real")
part1(lines)
part2(lines)