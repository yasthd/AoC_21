SAMPLE = r"""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

def parse_input(raw: str) -> list[str]:
    return [s for s in raw.strip().split("\n")]

def get_corrupt_points(line: str) -> int:
    stack = []
    opening = ["(", "[", "{", "<"]
    translation = {")":"(", "]":"[", "}":"{", ">":"<"}
    points = {")":3, "]":57, "}":1197, ">":25137}
    for character in line:
        if character in opening:
            stack.append(character)
        elif translation[character] == stack.pop():
            continue
        else:
            return points[character]
    return 0

def find_corrupt(lines: list[str]) -> int:
    score = 0
    for line in lines:
        score += get_corrupt_points(line)
    return score

def get_incomplete_line(line: str) -> str:
    stack = []
    opening = ["(", "[", "{", "<"]
    translation = {")":"(", "]":"[", "}":"{", ">":"<"}
    for character in line:
        if character in opening:
            stack.append(character)
        elif translation[character] == stack.pop():
            continue
        else:
            return None
    return "".join(stack)

def incomplete_points(incomplete_line: str) -> int:
    points = 0
    translation = {"(":1, "[":2, "{":3, "<":4}
    for char in incomplete_line[::-1]:
        points *= 5
        points += translation[char]
    return points

def find_incomplete(lines: list[str]) -> int:
    scores = []
    for line in lines:
        incomplete_line = get_incomplete_line(line)
        if incomplete_line:
            scores.append(incomplete_points(incomplete_line))
    return sorted(scores)[len(scores) // 2]


LINES = parse_input(SAMPLE)
assert find_corrupt(LINES) == 26397
assert find_incomplete(LINES) == 288957

with open("input") as f:
    lines = parse_input(f.read())

solution1 = find_corrupt(lines)
solution2 = find_incomplete(lines)
