from dataclasses import dataclass
from collections import OrderedDict

SAMPLE = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

@dataclass
class BingoBoard:
    board: list[OrderedDict[int, bool]]
    last_number: int = None
    won: bool = False
    score: int = 0
    place: int = 0

    @staticmethod
    def from_string(s: str) -> "BingoBoard":
        b = OrderedDict((int(n), False) for n in s.split())
        return BingoBoard(b)

    def add_number(self, number: int) -> None:
        if number in self.board.keys():
            self.board[number] = True
            self.last_number = number
            self.check_win()

    def check_win(self) -> None:
        index_board = list(self.board.items())
        #check rows
        for row in range(5):
            for column in range(5):
                item = index_board[row*5+column]
                if item[1]:
                    if column == 4:
                        self.won = True
                        return
                else:
                    break
        #check columns
        for column in range(5):
            for row in range(5):
                item = index_board[row*5+column]
                if item[1]:
                    if row == 4:
                        self.won = True
                        return
                else:
                    break

    def calculate_score(self) -> None:
        assert self.won == True
        self.score = self.last_number * sum([n for n, b in self.board.items() if not b])

def process_input(raw_input: str) -> tuple[list[int], list[BingoBoard]]:
    split_input = raw_input.strip().split("\n\n")
    draw = [int(n) for n in split_input[0].split(",")]
    boards = [BingoBoard.from_string(b) for b in split_input[1:]]
    return draw, boards

def winning_board_score(draw: list[int], boards: list[BingoBoard]) -> int:
    for number in draw:
        for board in boards:
            board.add_number(number)
            if board.won:
                board.calculate_score()
                return board.score

def last_winning_board_score(draw: list[int], boards: list[BingoBoard]) -> int:
    place = 1
    for number in draw:
        for board in boards:
            if not board.won:
                board.add_number(number)
                if board.won:
                    board.calculate_score()
                    board.place = place
                    place += 1
    return sorted(boards, key=lambda b: b.place, reverse=True)[0].score


DRAW, BOARDS = process_input(SAMPLE)
assert winning_board_score(DRAW, BOARDS) == 4512
assert last_winning_board_score(DRAW, BOARDS) == 1924

with open("input") as f:
    draw, boards = process_input(f.read())

solution1 = winning_board_score(draw, boards)
solution2 = last_winning_board_score(draw, boards)
