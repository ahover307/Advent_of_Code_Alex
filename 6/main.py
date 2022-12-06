import datetime

test_input = open('test_input.txt', 'r')
test_lines = test_input.readlines()

input_file = open('input.txt', 'r')
lines = input_file.readlines()


def part1(window, input):
    print("Part 1")

    for line in input:
        for i, l in enumerate(line):
            if i < window-1:
                continue

            sub = line[i-window+1:i+1]
            flag = False

            for j in range(window):
                if sub.count(line[i-j]) > 1:
                    flag = True


            if flag: continue

            print(i+1)
            break


print("Tests")
part1(4, test_lines)
part1(14, test_lines)

print()

print("Real")
start = datetime.datetime.now()
part1(4, lines)
end = datetime.datetime.now()
print(end-start)
start = datetime.datetime.now()
part1(14, lines)
end = datetime.datetime.now()
print(end-start)
