import unittest
from dsl import add_border, change_color, replace_color, connect_horizontal
from type import Color, Coordinates, Grid

class TestDSL(unittest.TestCase):
    def test_add_border(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        coordinates = {(1, 1)}
        result = add_border(grid, coordinates, 2)
        expected = [
            [2, 2, 2],
            [2, 1, 2],
            [2, 2, 2]
        ]
        self.assertEqual(result, expected)

    def test_change_color(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        coordinates = {(1, 1), (1, 2), (2, 1), (2, 2)}
        result = change_color(grid, coordinates, 2)
        expected = [
            [0, 0, 0, 0, 0],
            [0, 2, 2, 0, 0],
            [0, 2, 2, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(result, expected)

    def test_replace_color(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        result = replace_color(grid, 1, 3)
        expected = [
            [0, 0, 0, 0, 0],
            [0, 3, 3, 0, 0],
            [0, 3, 3, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(result, expected)

    def test_connect_horizontal(self):
        grid = [
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
        ]
        coordinates = {(0, 0), (0, 2), (0, 4), (0, 6), (1, 0), (1, 2), (1, 4), (1, 6), (2, 0), (2, 2), (2, 4), (2, 6)}
        result = connect_horizontal(grid, coordinates, 2)
        print("result", result)
        expected = [
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()