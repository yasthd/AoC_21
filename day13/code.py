from dataclasses import dataclass

SAMPLE = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

@dataclass(frozen=True)
class Dot:
    x: int
    y: int

@dataclass
class Instruction:
    axis: str
    line: int

def parse_input(raw: str) -> tuple[set[Dot], list[Instruction]]:
    raw_split = raw.strip().split("\n\n")
    dots = {Dot(int(line.split(",")[0]), int(line.split(",")[1])) for line in raw_split[0].split("\n")}
    instructions = [Instruction(line.split("=")[0][-1], int(line.split("=")[1])) for line in raw_split[1].split("\n")]
    return dots, instructions

def apply_fold(sheet: set[Dot], instruction: Instruction) -> set[Dot]:
    folding = {d for d in sheet \
                        if (d.y > instruction.line and instruction.axis == "y") \
                        or (d.x > instruction.line and instruction.axis == "x")}
    new_sheet = {d for d in sheet if d not in folding}
    for dot in folding:
        new_dot = Dot(dot.x, 2*instruction.line - dot.y) if instruction.axis == "y" \
                            else  Dot(2*instruction.line - dot.x, dot.y)
        new_sheet.update([new_dot])
    return new_sheet

def apply_instructions(sheet: set[Dot], instructions: list[Instruction], once: bool = True) -> set[Dot]:
    folds = 1 if once else len(instructions)
    for i in range(folds):
        sheet = apply_fold(sheet, instructions[i])
    return sheet

def print_sheet(sheet: set[Dot]) -> None:
    width = max([d.x for d in sheet]) +1
    height = max([d.y for d in sheet]) +1
    display = [[" "] * width for _ in range(height)]
    for dot in sheet:
        display[dot.y][dot.x] = "#"
    for row in display:
        print(" ".join(row))


SHEET, INSTRUCTIONS = parse_input(SAMPLE)
assert len(apply_instructions(SHEET, INSTRUCTIONS, False)) == 16

with open("input") as f:
    sheet, instructions = parse_input(f.read())

solution1 = len(apply_instructions(sheet, instructions))
solution2 = apply_instructions(sheet, instructions, False)
print_sheet(solution2) #readable with mono-font
