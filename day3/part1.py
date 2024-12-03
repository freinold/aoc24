import re

with open("input") as file:
    input = file.read()

pattern = r"mul\((?P<factor1>[0-9]{1,3}),(?P<factor2>[0-9]{1,3})\)"

multiplication_sum = 0

for item in re.finditer(pattern, input):
    factor1 = int(item.group("factor1"))
    factor2 = int(item.group("factor2"))
    multiplication = factor1 * factor2
    multiplication_sum += multiplication

print(f"Sum of all valid multiplications: {multiplication_sum}")
