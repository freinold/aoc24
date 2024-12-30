import math
from itertools import product

def concatenate_integers(integers: list[int]) -> int:
    concatenation = "".join(map(str, integers))
    return int(concatenation)

with open("input") as file:
    input_string = file.read()

equations: list[tuple[int, list[int]]] = []

for line in input_string.splitlines():
    test_value, numbers = line.split(sep=": ")
    test_value = int(test_value)
    numbers = list(map(lambda x: int(x), numbers.split(sep=" ")))
    equations.append((test_value, numbers))

total_calibration_result = 0

for test_value, numbers in equations:
    operator_combinations = product([sum, math.prod, concatenate_integers], repeat=len(numbers) - 1)
    for op_comb in operator_combinations:
        computed_value = numbers[0]
        for i in range(len(op_comb)):
            computed_value = op_comb[i]([computed_value, numbers[i+1]])
        
        if computed_value == test_value:
            total_calibration_result += test_value
            break

print(f"Total calibration result with concatenation: {total_calibration_result}")