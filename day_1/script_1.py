elves = []

with open("day_1\script_1_values.txt") as file:
    sum = []
    for line in file:
        if(not line.rstrip()):
            elves.append(sum)
            sum = []
        else:
            sum.append(int(line.rstrip()))

def calculateSum(elf: list) -> int:
    sum=0
    for value in elf:
        sum += value
    return sum

#Calculate the sum for each elf and find the highest number

highest_sum = 0
sum_list = []
for elf in elves:
    current_sum = calculateSum(elf)
    sum_list.append(current_sum)
    if(current_sum > highest_sum):
        highest_sum = current_sum

print(f"Highest sum: {highest_sum}")

#Sort the array using quicksort, return and add first three entries

def quicksort(input_values: list):
        
    length = len(input_values)
    if length <= 1:
        return input_values
    else:
        pivot = input_values.pop()
    
    smaller_than_pivot = []
    larger_than_pivot = []

    for sum in input_values:
        if(sum > pivot):
            larger_than_pivot.append(sum)
        else:
            smaller_than_pivot.append(sum)

    return quicksort(larger_than_pivot) + [pivot] + quicksort(smaller_than_pivot)

sum_list=quicksort(sum_list)

three_elves_sum = sum_list[0] + sum_list[1] + sum_list[2]
print(f"Calory-sum of first three elves: {three_elves_sum}") 

