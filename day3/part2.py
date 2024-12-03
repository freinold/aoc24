import re

with open("input") as file:
    input: str = file.read()

pattern: str = r"(?P<mul>mul\((?P<factor1>[0-9]{1,3}),(?P<factor2>[0-9]{1,3})\))|(?P<do>do\(\))|(?P<donz>don't\(\))"

multiplication_sum: int = 0
multiplication_enabled: bool = True

for match in re.finditer(pattern, input):
    if match[0].startswith("mul") and multiplication_enabled:
        factor1: int = int(match.group("factor1"))
        factor2: int = int(match.group("factor2"))
        multiplication: int = factor1 * factor2
        multiplication_sum += multiplication
    elif match[0].startswith("don't()"):
        multiplication_enabled = False
    elif match[0].startswith("do()"):
        multiplication_enabled = True


print(f"Sum of all valid multiplications: {multiplication_sum}")
