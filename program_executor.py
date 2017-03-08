from enum import Enum


class Direction(Enum):
    left = 1
    right = 2


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
        else:
            if self.location[0] == 0:
                self.running = False
            else:
                self.location[0] -= 1

    def run(self):
        while self.running:
            portal = self.matrix.get_symbol(self.location[0], self.location[1]).execute()
            if portal is not None:
                if portal.linked_portal is None:
                    self.running = False
                else:
                    if not portal.momentum:
                        self.direction = Direction.left if self.direction == Direction.right else Direction.right
                    self.location[0] = portal.linked_portal.x
                    self.location[1] = portal.linked_portal.y
            self.step()
