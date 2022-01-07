SAMPLE = """199
200
208
210
200
207
240
269
260
263"""

def get_number_increases(numbers: list[int]) -> int:
    counter = 0
    prev = numbers[0]
    for i in numbers[1:]:
        counter += 1 if i > prev else 0
        prev = i
    return counter

def get_window_increase(numbers: list[int]) -> int:
    counter = 0
    prev_window = sum(numbers[:3])
    numbers.pop(0)
    while len(numbers) >= 3:
        next_window = sum(numbers[:3])
        counter += 1 if next_window > prev_window else 0
        prev_window = next_window
        numbers.pop(0)
    return counter


NUMBERS = list(map(int, SAMPLE.strip().split("\n")))
assert get_number_increases(NUMBERS) == 7
assert get_window_increase(NUMBERS) == 5

with open("input") as f:
    sonar_sweep = list(map(int, f.read().strip().split("\n")))

solution1 = get_number_increases(sonar_sweep)
solution2 = get_window_increase(sonar_sweep)
