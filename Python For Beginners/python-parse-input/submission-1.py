from typing import List

def read_integers() -> List[int]:
    numbers = (input())
    number_list = [int(x) for x in numbers.split(",")]
    return number_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())