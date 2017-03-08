import time
from program_matrix import ProgramMatrix
from program_executor import ProgramExecutor


if __name__ == "__main__":
    start_time = time.time()
    text = open('code.p2p', 'r').read().replace(' ', '').replace('\n', '')
    matrix = ProgramMatrix(text, 100)
    executor = ProgramExecutor(matrix)
    executor.run()
    print("\n--- Program finished in %s seconds ---" % (time.time() - start_time))
