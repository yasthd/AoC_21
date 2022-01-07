from collections import Counter

SAMPLE  = "3,4,3,1,2"

def parse_input(raw: str) -> list[int]:
    raw_int = [int(i) for i in raw.strip().split(",")]
    counter = Counter(raw_int)
    return [counter[i] for i in range(9)]

def cycle(population: list[int]) -> list[int]:
    new_fish = population[0]
    new_population = population[1:]
    new_population[6] += new_fish
    return new_population + [new_fish]

def skip_time(population: list[int], days: int = 80) -> int:
    for _ in range(days):
        population = cycle(population)
    return sum(population)

POPULATION = parse_input(SAMPLE)
assert skip_time(POPULATION) == 5934
assert skip_time(POPULATION, days=256) == 26984457539

with open("input") as f:
    population = parse_input(f.read())

solution1 = skip_time(population)
solution2 = skip_time(population, days=256)
