input_file = open('input.txt', 'r')
lines = input_file.readlines()

# Part 1
print("Part 1")

current_max = 0
block = 0
for line in lines:
    if line == "\n":
        current_max = max(current_max, block)
        block = 0
    else:
        block += int(line)

print(current_max)

print()
# Part 2
print("Part 2")
array = []
block = 0
for line in lines:
    if line == '\n':
        array.append(block)
        block = 0
    else:
        block += int(line)

array.sort(reverse=True)
print("Top 3")
print(array[0])
print(array[1])
print(array[2])

print("Sum")
print(array[0] + array[1] + array[2])
