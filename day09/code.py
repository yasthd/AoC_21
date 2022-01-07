from dataclasses import dataclass
from math import prod

SAMPLE = """2199943210
                           3987894921
                           9856789892
                           8767896789
                           9899965678"""

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    height: int

def parse_input(raw: str) -> list[list[int]]:
    cave = []
    for line in raw.strip().split():
        cave.append([int(i) for i in line])
    return cave

def find_neighbors(point: Point, cave: list[list[int]]) -> list[Point]:
    neighbors  = []
    height = len(cave)
    width = len(cave[0])
    for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        n_x = point.x + x
        n_y = point.y + y
        if 0 <= n_x < width and 0 <= n_y < height:
            neighbors.append(Point(n_x, n_y, cave[n_y][n_x]))
    return neighbors

def find_lowpoints(cave: list[list[int]], part1: bool = False) -> list[Point]: # or -> int
    lowpoints = []
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            location = Point(x, y, cave[y][x])
            neighbors = find_neighbors(location, cave)
            neighbor_heights = [p.height for p in neighbors]
            if location.height < min(neighbor_heights):
                lowpoints.append(location)
    return lowpoints if not part1 else sum([p.height+1 for p in lowpoints])

def find_basins(cave: list[list[int]]) -> int:
    basins = []
    lowpoints = find_lowpoints(cave)
    for lowpoint in lowpoints:
        basin = set()
        todo = set([lowpoint])
        while todo:
            point = todo.pop()
            basin.update([point])
            todo.update([p for p in find_neighbors(point, cave) if (p.height != 9) and (p not in basin)])
        basins.append(len(basin))
    return prod(sorted(basins, reverse=True)[:3])


CAVE = parse_input(SAMPLE)
assert find_lowpoints(CAVE, True) == 15
assert find_basins(CAVE) == 1134

with open("input") as f:
    cave = parse_input(f.read())

solution1 = find_lowpoints(cave, True)
solution2 = find_basins(cave)
