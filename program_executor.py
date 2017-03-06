from enum import Enum


class Direction(Enum):
    left = 1
    right = 2
    up = 3
    down = 4


class ProgramExecutor:
    def __init__(self, matrix):
        self.location = [0, 0]
        self.direction = Direction.right
        self.matrix = matrix
        self.running = True

    def step(self):
        if self.direction == Direction.right:
            if self.location[0] + 1 == self.matrix.matrix_size:
                self.running = False
            else:
                self.location[0] += 1
        elif self.direction == Direction.left:
            if self.location[0] == 0:
                self.running = False
            else:
                self.location[0] -= 1
        elif self.direction == Direction.up:
            if self.location[0] == 0:
                self.running = False
            else:
                self.location[1] -= 1
        else:
            if self.location[0] + 1 == self.matrix.matrix_size:
                self.running = False
            else:
                self.location[1] += 1

    def run(self):
        while self.running:
            self.matrix.get_symbol(self.location[0], self.location[1]).execute()
            self.step()
