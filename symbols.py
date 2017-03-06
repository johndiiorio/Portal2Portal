class Empty:
    @staticmethod
    def execute(pointer, matrix):
        raise NotImplemented

    def __str__(self):
        return " "


class Plus:
    @staticmethod
    def execute(pointer, matrix):
        matrix[pointer[0]][pointer[1]] += 1

    def __str__(self):
        return "+"


class Minus:
    @staticmethod
    def execute(pointer, matrix):
        matrix[pointer[0]][pointer[1]] -= 1

    def __str__(self):
        return "-"


class Left:
    @staticmethod
    def execute(pointer):
        pointer[0] -= 1

    def __str__(self):
        return "<"


class Right:
    @staticmethod
    def execute(pointer):
        pointer[0] += 1

    def __str__(self):
        return ">"


class Output:
    @staticmethod
    def execute(pointer, matrix):
        print(str(chr(matrix[pointer[0]][pointer[1]])))

    def __str__(self):
        return "."


class Portal:
    def __init__(self, x, y, momentum=True):
        self.x = x
        self.y = y
        self.linked_portal = None
        self.momentum = momentum

    def link(self, portal):
        self.linked_portal = portal

    def execute(self):
        raise NotImplemented

    def __str__(self):
        return "(" if self.momentum else "{"
