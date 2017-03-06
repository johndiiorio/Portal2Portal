from symbols import *
import numpy as np


class ProgramMatrix:
    def __init__(self, text, matrix_size=15):
        if not self.is_valid(text):
            raise SyntaxError("Unexpected token error")
        try:
            self.matrix = np.array([[Empty() for i in range(matrix_size)] for j in range(matrix_size)], dtype=np.object)
            self.matrix_size = matrix_size
            locations = text.split("|")
            for location in locations:
                col, row = [int(x) for x in location[:location.index(":")].split(",")]
                self.add_input_to_matrix(location[location.index(":")+1:], row, col)
        except:
            raise SyntaxError("Invalid syntax") from None

    def __str__(self):
        s = ""
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                s += str(self.matrix[i][j])
            s += "\n"
        return s

    @staticmethod
    def is_valid(text):
        valid_chars = ["<", ">", "+", "-", "|", "{", "}", "(", ")", "[", "]", ".", ",", ":"]
        for i in text:
            if i not in valid_chars and not i.isdigit():
                return False
        return True

    def add_input_to_matrix(self, text, row, col):
        i = 0
        col_count = 0
        while i < len(text):
            if text[i] == "+":
                self.matrix[row][col+col_count] = Plus()
                i += 1
                col_count += 1
            elif text[i] == "-":
                self.matrix[row][col+col_count] = Minus()
                i += 1
                col_count += 1
            elif text[i] == "<":
                self.matrix[row][col+col_count] = Left()
                i += 1
                col_count += 1
            elif text[i] == ">":
                self.matrix[row][col+col_count] = Right()
                i += 1
                col_count += 1
            elif text[i] == ".":
                self.matrix[row][col+col_count] = Output()
                i += 1
                col_count += 1
            elif text[i] == "(" or text[i] == "{":
                skip = text[i:].index(")") + 1 if text[i] == "(" else text[i:].index("}") + 1
                x1, y1, x2, y2 = [int(x) for x in text[i+1:i+skip-1].split(",")]
                momentum = True if text[i] == "(" else False
                portal_open = Portal(x1, y1, momentum)
                portal_close = Portal(x2, y2, momentum)
                portal_open.link(portal_close)
                portal_close.link(portal_open)
                self.matrix[y1, x1] = portal_open
                self.matrix[y2, x2] = portal_close
                i += skip
            else:
                raise SyntaxError("Unexpected token error")