import datetime

from progress.bar import Bar

test_input = open('test_input.txt', 'r')
test_lines = test_input.readlines()

input_file = open('input.txt', 'r')
lines = input_file.readlines()

p = []
sizes = {}
directory = {}
folders = []


def calc_size_of_directory(size_of_file):
    # Look at entire path, and update the size of each directory touched
    for i in range(len(p)):
        # print("file: {} - type: {} - size: {} - add: {} - type: {}".format(i, type(sizes['/'.join(p)]), sizes['/'.join(p)], size_of_file, type(int(size_of_file))) )
        sizes['/'.join(p[: len(p) - i])] += int(size_of_file)


def find_matching_sizes(max_size):
    temp = 0
    for i in folders:
        # Directories can be counted multiple times
        if sizes[i] < max_size:
            temp += sizes[i]
    return temp


def new_matching_sizes(total_disk, target):
    # get total space used by disk
    total_used = sizes['/']

    # calculate how much we need
    current_free = total_disk - total_used
    currently_need = target - current_free
    # find min folder that we can delete

    temp = total_used
    for i in folders:
        # Look at all directories, keep the smallest that fits criteria
        if sizes[i] > currently_need:
            temp = min(temp, sizes[i])
    return temp


def part1(bar, input):
    print("Part 1")

    for line in input:
        # Strip line end character
        line = line.strip()
        # Is command
        if '$' in line:
            if 'cd' in line:
                if '..' in line:
                    # If we are going up a directory, pop off the path
                    p.pop()
                else:
                    # Manually keeping things after the command. Whatever. I know its not efficient
                    # We know we are going into a directory at this point
                    item = line.split('$ cd ')[1]

                    # Add item to the path
                    p.append(item)

                    # If it is a directory, then we need to remember that so i can count up folder sizes alter
                    folders.append('/'.join(p))
                    sizes[item] = 0
            else:
                # We could use actual logic and parse this command. but also. fuck that
                # Would it be more efficient? Yes.
                # Do I care - Not for this competition
                continue
        else:
            # This is a list of files within a given folder
            temp = line.split(' ')

            # While touching the file, add it to the path
            p.append(temp[1])

            # If it is a directory, I still need an entry, just it will be worth 0 at now
            file_size = 0
            if not 'dir' in line:
                # If it is not a directory, we need the size of the file saved
                file_size = temp[0]

            sizes['/'.join(p)] = int(file_size)
            # Update each level of folders
            calc_size_of_directory(size_of_file=file_size)

            # Now that we are not on the file anymore, pop the path
            p.pop()

        bar.next()


print("Tests")
# Set up progress bar
bar = Bar('Processing', max=len(test_lines))
part1(bar, test_lines)
print(find_matching_sizes(100000))
bar.finish()

p = []
sizes = {}
directory = {}
folders = []
bar = Bar('Processing', max=len(test_lines))
part1(bar, test_lines)
print(new_matching_sizes(70000000, 30000000))
bar.finish()

print()

print("Real")
# reset variables
p = []
sizes = {}
directory = {}
folders = []
bar = Bar('Progress', max=len(lines))
start = datetime.datetime.now()
part1(bar, lines)
print(find_matching_sizes(100000))
end = datetime.datetime.now()
print(end - start)
bar.finish()

# reset variables
p = []
sizes = {}
directory = {}
folders = []
bar = Bar('Progress', max=len(lines))
start = datetime.datetime.now()
part1(bar, lines)
print(new_matching_sizes(70000000, 30000000))
end = datetime.datetime.now()
print(end - start)
bar.finish()
