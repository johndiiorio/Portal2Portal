from ProgramMatrix import ProgramMatrix

if __name__ == "__main__":
    text = open('main.p2p', 'r').read().replace(' ', '').replace('\n', '')
    pointer = [0, 0]
    board = ProgramMatrix(text)
    print(board)
