with open("input") as file:
    input_str: str = file.read()

rules: list[tuple[str, str]] = list()
updates: list[list[str]] = list()

for line in input_str.splitlines():
    if "|" in line:
        rules.append(tuple(line.split("|")))
    elif "," in line:
        updates.append(line.split(","))

correct_update_middle_page_sum: int = 0

for update in updates:
    is_in_correct_order: bool = True
    for rule in rules:
        if not (rule[0] in update and rule[1] in update):
            continue
    
        if update.index(rule[0]) > update.index(rule[1]):
            is_in_correct_order = False
            break

    if is_in_correct_order:
        correct_update_middle_page_sum += int(update[len(update)//2])

print(f"Sum of middle pages for correctly-ordered updates: {correct_update_middle_page_sum}")