from tape import Tape
tape = Tape()


class Empty:
    @staticmethod
    def execute():
        pass

    def __str__(self):
        return " "


class Plus:
    @staticmethod
    def execute():
        tape.increment()

    def __str__(self):
        return "+"


class Minus:
    @staticmethod
    def execute():
        tape.decrement()

    def __str__(self):
        return "-"


class Left:
    @staticmethod
    def execute():
        tape.step_left()

    def __str__(self):
        return "<"


class Right:
    @staticmethod
    def execute():
        tape.step_right()

    def __str__(self):
        return ">"


class Output:
    @staticmethod
    def execute():
        print(str(chr(tape.get())))

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
        return self if not tape.get() == 0 else None

    def __str__(self):
        return "(" if self.momentum else "{"
