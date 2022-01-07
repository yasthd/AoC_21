import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path
from copy import deepcopy

SAMPLE = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

def parse_input(raw: str) -> tuple[nx.DiGraph, tuple[int, int], tuple[int, int]]:
    graph = nx.DiGraph()
    matrix = [[int(i) for i in line] for line in raw.strip().split("\n")]
    start = (0, 0)
    end = (len(matrix)-1, len(matrix[0])-1)
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            graph.add_node((x, y), height=matrix[y][x])
            neighbors = [(x+r, y+c) for r, c in ((-1, 0), (1, 0), (0, -1), (0, 1)) if 0 <= x+r < len(matrix[0]) and 0 <= y+c < len(matrix)]
            for n in neighbors:
                graph.add_edge(n, (x, y), weight=matrix[y][x])
    return graph, start, end

def lowest_risk(graph: nx.DiGraph, start: tuple[int, int], end: tuple[int, int]) -> int:
    path = shortest_path(graph, start, end, weight="weight")
    return(sum([graph.nodes[i]["height"] for i in path[1:]]))

def expand_map(raw: str) -> str:
    map = raw.strip().split("\n")
    width = len(map[0])
    height = len(map)
    # expand to the right
    for i in range(width*4):
        idx_column = i % width + (i // width) * width
        for idx_row in range(height):
            map[idx_row] += str(max((int(map[idx_row][idx_column]) + 1) % 10, 1))
    # expand downwards
    for i in range(height*4):
        new_line = ""
        idx_row = i % height + (i // height) * height
        for idx_column in range(width*5):
            new_line += str(max((int(map[idx_row][idx_column]) + 1) % 10, 1))
        map.append(new_line)
    return "\n".join(map)


GRAPH, START, END = parse_input(deepcopy(SAMPLE))
EXPANDED = expand_map(SAMPLE)
XGRAPH, XSTART, XEND = parse_input(EXPANDED)
assert lowest_risk(GRAPH, START, END) == 40
assert lowest_risk(XGRAPH, XSTART, XEND) == 315

with open("input") as f:
    raw = f.read()
    graph, start, end = parse_input(deepcopy(raw))
    expanded = expand_map(raw)
    xgraph, xstart, xend = parse_input(expanded)

solution1 = lowest_risk(graph, start, end)
solution2 = lowest_risk(xgraph, xstart, xend)
