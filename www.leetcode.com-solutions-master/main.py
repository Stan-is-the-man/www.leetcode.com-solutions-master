# Task
# You are given a string .
# Your task is to find the indices of the start and end of string  in .

first = input('Please enter the main string\n')
second = input('Please enter the str to be compared\n')

for x in range(len(first) - (len(second) - 1)):
    current_to_compare = ''
    indexes = []
    current_x_index = x
    for y in range(len(second)):
        indexes.append(current_x_index)
        current_x_index += 1
        current_to_compare += first[x+y]

    if current_to_compare == second:
        print(tuple(indexes))
