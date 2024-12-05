with open("input") as file:
    input_str: str = file.read()

rules: list[tuple[str, str]] = list()
updates: list[list[str]] = list()

for line in input_str.splitlines():
    if "|" in line:
        rules.append(tuple(line.split("|")))
    elif "," in line:
        updates.append(line.split(","))

incorrectly_ordered_updates: list[list[str]] = list()

for update in updates:
    is_in_correct_order: bool = True
    for rule in rules:
        if not (rule[0] in update and rule[1] in update):
            continue
    
        if update.index(rule[0]) > update.index(rule[1]):
            incorrectly_ordered_updates.append(update)
            break

reordered_update_middle_page_sum: int = 0

while len(incorrectly_ordered_updates) > 0:
    is_in_correct_order: bool = True
    update: list[str] = incorrectly_ordered_updates.pop()
    for rule in rules:
        if not (rule[0] in update and rule[1] in update):
            continue

        predecessor_index = update.index(rule[0])
        sucessor_index = update.index(rule[1])
        
        if predecessor_index > sucessor_index:
            update[predecessor_index] = rule[1]
            update[sucessor_index] = rule[0]
            incorrectly_ordered_updates.append(update)
            is_in_correct_order = False
            break

    if is_in_correct_order:
        reordered_update_middle_page_sum += int(update[len(update)//2])

print(f"Sum of middle pages for correctly-ordered updates: {reordered_update_middle_page_sum}")