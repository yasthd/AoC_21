import networkx as nx
from copy import deepcopy
from collections import Counter

SAMPLE = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

def create_graph(raw: str) -> nx.Graph:
    G = nx.Graph()
    edges = [(line.split("-")[0], line.split("-")[1]) for line in raw.strip().split("\n")]
    G.add_edges_from(edges)
    return G

def small_cave_twice(path: list[str]) -> bool:
    doubles = [True for cave, count in Counter(path).items() if count > 1 and cave.islower()]
    return any(doubles)

def find_paths(G: nx.Graph, visit_twice: bool = False) -> int:
    paths = []
    todo = [["start"]]
    while todo:
        path = todo.pop()
        end_node = path[-1]
        if end_node == "end":
            paths.append(path)
            continue
        for neighbor in G.neighbors(end_node):
            if (neighbor.islower() and neighbor in path and not visit_twice) \
            or (neighbor.islower() and neighbor in path and visit_twice and small_cave_twice(path)) \
            or (neighbor == "start"):
                continue
            new_path = deepcopy(path)
            new_path.append(neighbor)
            todo.append(new_path)
    return len(paths)


CAVE_SYSTEM = create_graph(SAMPLE)
assert find_paths(CAVE_SYSTEM) == 19
assert find_paths(CAVE_SYSTEM, True) == 103

with open("input") as f:
    puzzle_cave_system = create_graph(f.read())

solution1 = find_paths(puzzle_cave_system)
solution2 = find_paths(puzzle_cave_system, True)
