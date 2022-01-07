from collections import Counter

SAMPLE = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

def parse_input(raw: str) -> list[tuple[list[str], list[str]]]:
    entries = []
    for entry in raw.strip().split("\n"):
        entry_split = entry.split(" | ")
        signal_pattern = entry_split[0].split()
        output_value = entry_split[1].split()
        entries.append((signal_pattern, output_value))
    return entries

def count_number(number: int, output_value: list[str]) -> int:
    d = {1:2, 4:4, 7:3, 8:7}
    count = 0
    for digit in output_value:
        if len(digit) == d[number]:
            count += 1
    return count

def part_one(entries: list[tuple[list[str], list[str]]]) -> int:
    c = Counter()
    for i in [1, 4, 7, 8]:
        for entry in entries:
            c[i] += count_number(i, entry[1])
    return sum(c.values())

def sort_digit(digit: str) -> str:
    return "".join(sorted(digit))

def translator(signal_pattern: list[str]) -> dict[str, int]:
    cf = [i for i in signal_pattern if len(i) == 2][0]
    bcdf = [i for i in signal_pattern if len(i) == 4][0]
    acf = [i for i in signal_pattern if len(i) == 3][0]
    abcdefg = "abcdefg"
    zero_six_nine = [i for i in signal_pattern if len(i) == 6]
    cde = "".join([i for i in abcdefg for number in zero_six_nine if i not in number])
    aeg = "".join([i for i in abcdefg if i not in bcdf])
    acdeg = "".join(set(aeg + cde))
    bf = "".join([i for i in abcdefg if i not in acdeg])
    abcefg = "".join(set(aeg + bf + cf))
    f = [i for i in cf if i not in acdeg][0]
    c = [i for i in cf if i != f][0]
    abdefg = "".join([i for i in abcdefg if i != c])
    abcdfg = [i for i in zero_six_nine if sorted(i) not in [sorted(abcefg), sorted(abdefg)]][0]
    e = [i for i in abcdefg if i not in abcdfg][0]
    abdfg = "".join([i for i in abcdefg if i not in [c, e]])
    acdfg = [number for number in signal_pattern if (len(number) == 5) and (sorted(number) not in [sorted(acdeg), sorted(abdfg)])][0]
    return {sort_digit(abcefg): 0, sort_digit(cf): 1, sort_digit(acdeg): 2, sort_digit(acdfg): 3,
                   sort_digit(bcdf): 4, sort_digit(abdfg): 5, sort_digit(abdefg): 6, sort_digit(acf): 7,
                   sort_digit(abcdefg): 8, sort_digit(abcdfg): 9}

def part_two(entries: list[tuple[list[str], list[str]]]) -> int:
    counter = 0
    for entry in entries:
        translation_table = translator(entry[0])
        number = ""
        for digit in entry[1]:
            number += str(translation_table[sort_digit(digit)])
        counter += int(number)
    return counter


PUZZLE = parse_input(SAMPLE)
assert part_one(PUZZLE) == 26
assert part_two(PUZZLE) == 61229

with open("input") as f:
    puzzle = parse_input(f.read())

solution1 = part_one(puzzle)
solution2 = part_two(puzzle)
