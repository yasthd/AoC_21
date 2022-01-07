import re
from dataclasses import dataclass
from collections import Counter

SAMPLE  = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

@dataclass(frozen=True)
class Point:
    x: int
    y: int

@dataclass
class Vent:
    start: Point
    end: Point

    @staticmethod
    def from_line(line: str) -> "Vent":
        rgx = r"(\d+),(\d+) -> (\d+),(\d+)"
        start_x, start_y, end_x, end_y = re.search(rgx, line).groups()
        return Vent(Point(int(start_x), int(start_y)), Point(int(end_x), int(end_y)))

    def is_straight(self) -> bool:
        if (self.start.x == self.end.x) or (self.start.y == self.end.y):
            return True
        else:
            return False

    def get_points(self) -> set[Point]:
        points = set()
        if self.is_straight():
            for x in range(min(self.start.x, self.end.x), max(self.start.x, self.end.x)+1):
                points.add(Point(x, self.start.y))
            for y in range(min(self.start.y, self.end.y), max(self.start.y, self.end.y)+1):
                points.add(Point(self.start.x, y))
        else:
            if self.start.y < self.end.y:
                if self.start.x < self.end.x:
                    for i in range(abs(self.start.x - self.end.x)+1):
                        points.add(Point(self.start.x+i, self.start.y+i))
                else:
                    for i in range(abs(self.start.x - self.end.x)+1):
                        points.add(Point(self.start.x-i, self.start.y+i))
            else:
                if self.start.x < self.end.x:
                    for i in range(abs(self.start.x - self.end.x)+1):
                        points.add(Point(self.start.x+i, self.start.y-i))
                else:
                    for i in range(abs(self.start.x - self.end.x)+1):
                        points.add(Point(self.start.x-i, self.start.y-i))
        return points

def parse_input(input_string: str) -> list[Vent]:
    rgx = r"(\d+),(\d+) -> (\d+),(\d+)"
    return [Vent.from_line(line) for line in input_string.strip().split("\n")]

def find_overlaps(vents: list[Vent], part1: bool = False) -> int:
    points = []
    for vent in vents:
        if part1 and not vent.is_straight():
            continue
        points.extend(vent.get_points())
    counter = Counter(points)
    return len([p for p, c in counter.items() if c > 1])

VENTS = parse_input(SAMPLE)
assert find_overlaps(VENTS, True) == 5
assert find_overlaps(VENTS) == 12

with open("input") as f:
    vents = parse_input(f.read())

solution1 = find_overlaps(vents, True)
solution2 = find_overlaps(vents)
