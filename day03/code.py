from collections import Counter

SAMPLE = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".strip().split("\n")

def calculate_gamma_epsilon(numbers: list[str]) -> int:
    gamma = ""
    epsilon = ""
    for i in range(len(numbers[0])):
        column = [num[i] for num in numbers]
        count = Counter(column)
        gamma += count.most_common(1)[0][0]
        epsilon += str(int(not int(gamma[i])))
    return int(gamma, 2) * int(epsilon, 2)

def calculate_oxygen(numbers: list[str]) -> int:
    for i in range(len(numbers[0])):
        if len(numbers) == 1:
            break
        column = [num[i] for num in numbers]
        count = Counter(column)
        most_common = count.most_common()
        if most_common[0][1] == most_common[1][1]: #tie
            most_common = "1"
        else:
            most_common = most_common[0][0]
        numbers = list(filter(lambda num: num[i] == most_common, numbers))
    return int(numbers[0], 2)

def calculate_scrubber(numbers: list[str]) -> int:
    for i in range(len(numbers[0])):
        if len(numbers) == 1:
            break
        column = [num[i] for num in numbers]
        count = Counter(column)
        most_common = count.most_common()
        if most_common[0][1] == most_common[1][1]: #tie
            most_common = "0"
        else:
            most_common = most_common[1][0]
        numbers = list(filter(lambda num: num[i] == most_common, numbers))
    return int(numbers[0], 2)

assert calculate_gamma_epsilon(SAMPLE) == 198
assert calculate_oxygen(SAMPLE) == 23
assert calculate_scrubber(SAMPLE) == 10

with open("input") as f:
    report = f.read().strip().split("\n")

solution1 = calculate_gamma_epsilon(report)
solution2 = calculate_oxygen(report) * calculate_scrubber(report)
