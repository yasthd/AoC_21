from collections import Counter

SAMPLE = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

def parse_input(raw: str) -> tuple[str, dict[str, str]]:
    template, rules = raw.strip().split("\n\n")
    return template, {line.split()[0]:line.split()[-1] for line in rules.split("\n")}

def step(template: Counter[str], rules: dict[str, str]) -> Counter[str]:
    new_template = Counter()
    for pair in template:
        quantity = template[pair]
        if pair in rules:
            new_pair1 = pair[0] + rules[pair]
            new_pair2 = rules[pair] + pair[1]
            new_template[new_pair1] += quantity
            new_template[new_pair2] += quantity
        else:
            new_template[pair] += quantity
    return new_template

def calculate_score(template: Counter[str], last_char: str) -> int:
    scores = Counter()
    for pair in template:
        scores[pair[0]] += template[pair]
    scores[last_char] += 1
    return scores.most_common()[0][1] - scores.most_common()[-1][1]

def apply_steps(template: str, rules: dict[str, str], steps: int) -> int:
    last_char = template[-1]
    template = Counter([template[i]+template[i+1] for i in range(len(template)-1)])
    for _ in range(steps):
        template = step(template, rules)
    return calculate_score(template, last_char)


TEMPLATE, RULES = parse_input(SAMPLE)
assert apply_steps(TEMPLATE, RULES, 10) == 1588
assert apply_steps(TEMPLATE, RULES, 40) == 2188189693529

with open("input") as f:
    template, rules = parse_input(f.read())

solution1 = apply_steps(template, rules, 10)
solution2 = apply_steps(template, rules, 40)
