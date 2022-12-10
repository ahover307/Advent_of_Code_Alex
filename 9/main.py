from __future__ import annotations

import datetime

from progress.bar import Bar

test_input = open('test_input.txt', 'r')
test_lines = test_input.readlines()

test_input2 = open('test_input2.txt', 'r')
test_lines2 = test_input2.readlines()

input_file = open('input.txt', 'r')
lines = input_file.readlines()


class Snake:
    name: int
    x: int
    y: int
    child_leg: Snake
    movement: int
    space_hit: [(int, int)]

    def __init__(self, x, y, length_of_snake):
        self.x = x
        self.y = y
        self.movement = 1
        self.space_hit = [(0, 0)]  # because of the starting square
        self.name = length_of_snake
        if length_of_snake > 1:
            self.child_leg = Snake(x, y, length_of_snake - 1)

    def snake_length(self):
        try:
            self.child_leg.snake_length()
            print('>')
        except AttributeError:
            print('>')

    def get_tail_total_movement(self):
        try:
            return self.child_leg.get_tail_total_movement()
        except AttributeError:
            return self.movement

    def get_all_nodes_movements(self):
        try:
            return self.child_leg.get_all_nodes_movements() + self.movement
        except AttributeError:
            return self.movement

    def get_all_nodes_unique_movements(self):
        try:
            return self.child_leg.get_all_nodes_movements() + len(self.space_hit)
        except AttributeError:
            return len(self.space_hit)

    def get_tail_unique_movement(self):
        try:
            return self.child_leg.get_tail_unique_movement()
        except AttributeError:
            return len(self.space_hit)

    def add_to_spaces_hit(self, coords: (int, int)):
        if coords not in self.space_hit:
            self.space_hit.append(coords)

    def check_children(self, parent: Snake):
        try:
            # I hate this method. I hate it hate it hate it

            # Slide one closer to the parent
            # Parent is to the flat right
            if parent.x > self.x and parent.y == self.y:
                self.x += 1
            # Parent is to the flat left
            elif parent.x < self.x and parent.y == self.y:
                self.x -= 1
            # parent is to the flat up
            elif parent.y > self.y and parent.x == self.x:
                self.y += 1
            # parent is to the flat down
            elif parent.y < self.y and parent.x == self.x:
                self.y -= 1
            # Is diagonal top right
            elif parent.x > self.x and parent.y > self.y:
                self.x += 1
                self.y += 1
            # Parent is diagonal top left
            elif parent.x < self.x and parent.y > self.y:
                self.x -= 1
                self.y += 1
            # Parent is diagonal bottom right
            elif parent.x > self.x and parent.y < self.y:
                self.x += 1
                self.y -= 1
            # Bottom left
            elif parent.x < self.x and parent.y < self.y:
                self.x -= 1
                self.y -= 1

            self.movement += 1
            self.add_to_spaces_hit((self.x, self.y))
            self.child_leg.update_tail(self)
        except AttributeError:
            return

    def update_tail(self, parent: Snake):
        if abs(parent.x - self.x) == 2:
            self.check_children(parent)
        elif abs(parent.y - self.y) == 2:
            self.check_children(parent)

    def move_right(self):
        self.x += 1
        self.movement += 1
        self.add_to_spaces_hit((self.x, self.y))
        try:
            self.child_leg.update_tail(self)
        except AttributeError:
            return

    def move_left(self):
        self.x -= 1
        self.movement += 1
        self.add_to_spaces_hit((self.x, self.y))
        try:
            self.child_leg.update_tail(self)
        except AttributeError:
            return

    def move_up(self):
        self.y += 1
        self.movement += 1
        self.add_to_spaces_hit((self.x, self.y))
        try:
            self.child_leg.update_tail(self)
        except AttributeError:
            return

    def move_down(self):
        self.y -= 1
        self.movement += 1
        self.add_to_spaces_hit((self.x, self.y))
        try:
            self.child_leg.update_tail(self)
        except AttributeError:
            return


def solution(input: [str], part: int, length_of_snake: int):
    print("Part {}".format(part))

    snake = Snake(0, 0, length_of_snake)

    bar = Bar('Explore snake', max=len(input))
    for line in input:
        # Strip line end character
        line = line.strip()

        temp = line.split(" ")
        direction = temp[0]
        amount = int(temp[1])
        for i in range(amount):
            # Move the head
            if direction == 'R':
                snake.move_right()
            elif direction == 'U':
                snake.move_up()
            elif direction == 'L':
                snake.move_left()
            elif direction == 'D':
                snake.move_down()

        bar.next()
    bar.finish()

    print("Unique Moves: {}".format(snake.get_all_nodes_unique_movements()))
    print("Total Moves: {}".format(snake.get_all_nodes_movements()))
    print('Total score: {}'.format(snake.get_tail_unique_movement()))


print("Tests")
solution(test_lines, 1, 2)
solution(test_lines, 2, 10)
solution(test_lines2, 2, 10)

print()

print("Real")
start = datetime.datetime.now()
solution(lines, 1, 2)
end = datetime.datetime.now()
print(end - start)

start = datetime.datetime.now()
solution(lines, 2, 10)
end = datetime.datetime.now()
print(end - start)
