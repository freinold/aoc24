# Day 1 Advent of Code 2024 - Part 1

left_list = list()
right_list = list()

with open("input") as file:
    for line in file.readlines():
        left_val, right_val = line.split()
        left_list.append(int(left_val))
        right_list.append(int(right_val))

left_list = sorted(left_list)
right_list = sorted(right_list)

similarity_score = 0

for left_val, right_val in zip(left_list, right_list):
    difference = abs(left_val - right_val)
    similarity_score += difference

print(f"Similarity score by sorted difference: {similarity_score}")