class Tape:
    def __init__(self, size=1000):
        self.size = size
        self.data = [0]*size
        self.pointer = 500

    def __str__(self):
        return self.data

    def step_left(self):
        if self.pointer - 1 < 0:
            raise SyntaxError("Pointer out of bounds") from None
        self.pointer -= 1

    def step_right(self):
        if self.pointer + 1 > self.size:
            raise SyntaxError("Pointer out of bounds") from None
        self.pointer += 1

    def increment(self):
        self.data[self.pointer] += 1

    def decrement(self):
        self.data[self.pointer] -= 1

    def get(self):
        return self.data[self.pointer]
