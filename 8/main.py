import datetime

from progress.bar import Bar

test_input = open('test_input.txt', 'r')
test_lines = test_input.readlines()

input_file = open('input.txt', 'r')
lines = input_file.readlines()


def visible_from_outside(trees, x, y):
    tree_height = trees[x][y]
    end_of_array = len(trees) - 1

    if x == 0 or y == 0 or x == end_of_array or y == end_of_array:
        return True

    # Check the left
    left = True
    for i in range(y):
        if trees[x][i] >= tree_height:
            left = False

    # Visible from the left
    if left:
        return True

    # Check the right
    right = True
    for i in range(end_of_array - y):
        if trees[x][
            y + i + 1] >= tree_height:  # +1 since range is 0 based, and we don't want to start at the same value as y
            right = False

    # Visible from the right
    if right:
        return True

    # Check the north
    north = True
    for i in range(x):
        if trees[i][y] >= tree_height:
            north = False

    # Visible from the north
    if north:
        return True

    # Check the south
    south = True
    for i in range(end_of_array - x):
        if trees[x + i + 1][
            y] >= tree_height:  # +1 since range is 0 based, and we don't want to start at the same value as x
            south = False

    # Visible from the south
    if south:
        return True

    return False


def scenic_score(trees, x, y):
    values = [0, 0, 0, 0]
    end_of_array = len(trees) - 1

    if x == 2 and y == 3:
        print(trees[x][y])

    # Check the north
    for i in range(x - 1, -1, -1):
        values[0] += 1
        if i == 0 or trees[i][y] >= trees[x][y]:
            break

    # Check the left
    for i in range(y - 1, -1, -1):
        values[1] += 1
        if i == 0 or trees[x][i] >= trees[x][y]:
            break

    # Check the south
    for i in range(x + 1, end_of_array + 1):
        values[2] += 1
        if i == end_of_array or trees[i][y] >= trees[x][y]:
            break

    # Check the right
    for i in range(y + 1, end_of_array + 1):
        values[3] += 1
        if i == end_of_array or trees[x][i] >= trees[x][y]:
            break

    if x == 2 and y == 3:
        print(values)

    return values[0] * values[1] * values[2] * values[3]


def solution(input, part):
    print("Part {}".format(part))

    trees = []

    bar = Bar('Setup Data', max=len(input))
    for line in input:
        # Strip line end character
        line = line.strip()

        row = []
        for tree in line:
            tree_height = int(tree)
            row.append(tree_height)
        trees.append(row)
        bar.next()
    bar.finish()

    if len(trees) == 0:
        print('Zero trees parsed')
        return

    score = 0

    # Parse data
    bar = Bar('Parse data', max=len(trees) * len(trees[0]))
    # Check every tree on every row
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            if part == 1:
                if visible_from_outside(trees, i, j):
                    score += 1
            elif part == 2:
                temp_score = scenic_score(trees, i, j)
                # print("x: {}, y: {}, score: {}".format(i, j, temp_score))
                score = max(score, temp_score)

            bar.next()
    bar.finish()

    print('Total score: {}'.format(score))


print("Tests")
# Set up progress bar
solution(test_lines, 1)
solution(test_lines, 2)

print()

print("Real")
# reset variables

start = datetime.datetime.now()
solution(lines, 1)
end = datetime.datetime.now()
print(end - start)

start = datetime.datetime.now()
solution(lines, 2)
end = datetime.datetime.now()
print(end - start)
