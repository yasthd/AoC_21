from statistics import median, mean

SAMPLE = "16,1,2,0,4,2,7,1,2,14"
NUMBERS = [int(i) for i in SAMPLE.split(",")]

def calculate_fuel(crabs: list[int], position: int, crab_movement: bool = False) -> int:
    if not crab_movement:
        return sum([abs(i - position) for i in crabs])
    else:
        return sum([sum(range(1, abs(i - position)+1)) for i in crabs])

MEDIAN = int(median(NUMBERS))
MEAN = round(mean(NUMBERS))
assert calculate_fuel(NUMBERS, MEDIAN) == 37
assert calculate_fuel(NUMBERS, MEAN, True) == 168

with open("input") as f:
    numbers = [int(i) for i in f.read().strip().split(",")]

median = int(median(numbers))
mean = round(mean(numbers))
solution1 = calculate_fuel(numbers, median)
solution2 = min([calculate_fuel(numbers, i, True) for i in range(median, mean)]) # didn't work with mean
