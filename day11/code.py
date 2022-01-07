from dataclasses import dataclass
from copy import deepcopy

SAMPLE = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

@dataclass(frozen=True)
class Octopus:
    x: int
    y: int

def parse_input(raw: str) -> list[list[int]]:
    cavern = []
    for line in raw.strip().split():
        cavern.append([int(i) for i in line])
    return cavern

def find_neighbors(octopus: Octopus, cavern: list[list[int]]) -> list[Octopus]:
    neighbors  = []
    height = len(cavern)
    width = len(cavern[0])
    for x, y in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        n_x = octopus.x + x
        n_y = octopus.y + y
        if 0 <= n_x < width and 0 <= n_y < height:
            neighbors.append(Octopus(n_x, n_y))
    return neighbors

def increase_energy(cavern: list[list[int]]) -> list[list[int]]:
    height = len(cavern)
    width = len(cavern[0])
    for h in range(height):
        for w in range(width):
            cavern[h][w] += 1
    return cavern

def flash(cavern: list[list[int]]) -> tuple[list[list[int], int]]:
        height = len(cavern)
        width = len(cavern[0])
        flashed = set()
        todo = set()
        for h in range(height):
            for w in range(width):
                if cavern[h][w] > 9:
                    todo.update([Octopus(w, h)])
        while todo:
            octo_iq = todo.pop() #iq = in question
            if cavern[octo_iq.y][octo_iq.x] > 9:
                flashed.update([octo_iq])
                for octo_neighbor in find_neighbors(octo_iq, cavern):
                        if octo_neighbor not in flashed:
                            cavern[octo_neighbor.y][octo_neighbor.x] += 1
                            todo.update([octo_neighbor])
        return cavern, len(flashed)

def reset_energy(cavern: list[list[int]]) -> list[list[int]]:
    height = len(cavern)
    width = len(cavern[0])
    for h in range(height):
        for w in range(width):
            if cavern[h][w] > 9:
                cavern[h][w] = 0
    return cavern

def check_synchro(cavern: list[list[int]]) -> bool:
    height = len(cavern)
    width = len(cavern[0])
    for h in range(height):
        for w in range(width):
            if cavern[h][w] != 0:
                return False
    return True

def print_cavern(cavern: list[list[int]]):
    for line in cavern:
        print("".join([str(i) for i in line]))

def simulation(cavern: list[list[int]], steps: int = 100, synchro: bool = False) -> int:
    total_flashes = 0
    for i in range(steps):
        cavern = increase_energy(cavern)
        cavern, flashes = flash(cavern)
        cavern = reset_energy(cavern)
        total_flashes += flashes
        if synchro and check_synchro(cavern):
            return i + 1
    return total_flashes


CAVERN = parse_input(SAMPLE)
assert simulation(deepcopy(CAVERN)) == 1656
assert simulation(CAVERN, 1000, True) == 195

with open("input") as f:
    cavern = parse_input(f.read())

solution1 = simulation(deepcopy(cavern))
solution2 = simulation(cavern, 1000, True)
