"""
https://adventofcode.com/2018/day/3
"""

import re

input_file = 'day03/p01_input.txt'

def get_input(filename):
    with open(filename) as f:
        return f.readlines()

class Fabric():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[-1] * width for _ in range(height)]

    def match_piece(self, piece):
        for idy, row in enumerate(self.grid[piece.y:piece.y + piece.height]):
            for idx, _ in enumerate(row[piece.x:piece.x + piece.width]):
                tmp_x = idx + piece.x
                tmp_y = idy + piece.y
                if self.grid[tmp_y][tmp_x] == -1:
                    self.grid[tmp_y][tmp_x] = 0
                elif self.grid[tmp_y][tmp_x] == 0:
                    self.grid[tmp_y][tmp_x] = 1
                else:
                    continue

    def get_overlap(self):
        return sum([sum([1 for col in row if col == 1]) for row in self.grid])

class PieceOfFabric():
    def __init__(self):
        self.id = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None

    @classmethod
    def parse_from_string(cls, input_string):
        """
        Example: #1 @ 555,891: 18x12
        """
        pattern = r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)'
        match = re.match(pattern, input_string)

        if match:
            tmp = cls()
            tmp.id = int(match.group(1))
            tmp.x = int(match.group(2))
            tmp.y = int(match.group(3))
            tmp.width = int(match.group(4))
            tmp.height = int(match.group(5))
            return tmp

def main():
    test_data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    test_obj = [PieceOfFabric.parse_from_string(item) for item in test_data]
    test_fabric = Fabric(8, 8)

    for item in test_obj:
        test_fabric.match_piece(item)

    assert test_fabric.get_overlap() == 4

    raw_data = get_input(input_file)
    parsed_data = [PieceOfFabric.parse_from_string(line) for line in raw_data]
    fabric = Fabric(1000, 1000)

    for item in parsed_data:
        fabric.match_piece(item)

    print(fabric.get_overlap())

if __name__ == "__main__":
    main()
