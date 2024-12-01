# Day 1 Advent of Code 2024 - Part 2

left_list = list()
right_list = list()

with open("input") as file:
    for line in file.readlines():
        left_val, right_val = line.split()
        left_list.append(int(left_val))
        right_list.append(int(right_val))

similarity_score = 0

for left_val in left_list:
    n_occurences = right_list.count(left_val)
    similarity_score += n_occurences * left_val

print(f"Similarity score by occurence: {similarity_score}")