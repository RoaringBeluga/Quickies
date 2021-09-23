
# Press the green button in the gutter to run the script.
from puzzles.puzzle_1 import test_the_count, most_frequent, Input

if __name__ == '__main__':
    test_the_count()
    result = most_frequent(Input, 7)
    print(f"Running with Caesar's: {result}")