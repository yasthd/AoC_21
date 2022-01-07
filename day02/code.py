SAMPLE = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def calculate_position(instructions: str) -> int:
    commands = [tuple(line.split()) for line in instructions.strip().split("\n")]
    depth = 0
    horizontal = 0
    for direction, distance in commands:
        if direction == "forward":
            horizontal += int(distance)
        elif direction == "down":
            depth += int(distance)
        elif direction == "up":
            depth -= int(distance)
    return depth * horizontal

def calculate_with_aim(instructions: str) -> int:
    commands = list(map(lambda line: (line[0], int(line[1])), [tuple(line.split()) for line in instructions.strip().split("\n")]))
    aim = 0
    depth = 0
    horizontal = 0
    for direction, distance in commands:
        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    return depth * horizontal


assert calculate_position(SAMPLE) == 150
assert calculate_with_aim(SAMPLE) == 900

with open("input") as f:
    puzzle_input = f.read()

solution1 = calculate_position(puzzle_input)
solution2 = calculate_with_aim(puzzle_input)
