import unittest
import numpy as np
import sys
from copy import copy

sys.setrecursionlimit(10000)

data = """
............#.............#......................#....#....................................................#..............#.......
..................................#...#......#.......#........#..................#....#...........................##....#.........
...........#...........#...........#...#...#...............................#.......................##....................#........
..................#.............#........#.....................#...........................................................#......
....#............................................................#..#...#......#.#......#...#..........#..#.....#....#...#........
.................................#......##.............................#..........................#...#.........#.................
.#.............#.........#..#..............................................................................##...........#..#......
....#..............#..........................##......#........#...#........#..........#........#.............#...................
.....#.......#..#......#..#..................................................................#.........................#..........
......................#...............................#......#................................#......#.....#......................
.......#.........#.....................................................................#....#.#.....................#.........#...
........................#......##..........#....#..........................#....................#...................#.........#...
................#..#............#...#.................................................................#...........#...............
.#.....#.....................#..........................................#................................#........................
.............#.##........#......#......#......................#..................................................#...#..........#.
.......#.........#.#..........#.............#.......#............#.....................#..........................................
.............................#.........................................................#.........#.........#.............#........
....#..#.#..................................................#...........#..................#....#.................................
...............#..........#.....#..............................................................#..................................
.......##.............................................................................#...............#.........#.................
....#.....#..........................#..........#................................#....................#...#.......................
.#.................................................#..#.....#.....................................................................
...........................#..............#.#...#..........................................#......#..........................#....
.#....#........#....................................................#...........................................#.................
...#..................#................##...#.............#..#....................#...............#...............................
..................................................#......#..........................................................#...#.........
#.#....................................#........#.............................................................#...................
...............................................#.......##...............................................#.........................
...#.............#................................................................................................................
.......................................#....#..#........#............#..........#.........#...#..................#................
........#.................................................#.........................................#...........#.................
...................#...........#...............................#..........................#................#..#..........#.....#..
...............#......#...............................................................#............................##..#.....##...
.........................................##.#..#..................#.......#.....................#.................................
...........#...................................................................#...#..................................#.....#.....
......#...............................#.......###..........................#....#.....................................#...........
.....##...............................#...................................................#................................#...#..
..................#....#.......#.......................................................................##.........................
.....#..#.................................................................................................#.......................
.#.................................#......................##....................................#..........................##.....
#.#................#......................................#...........................#.......#...................................
.................................#.......#.....#..............................................##..#....................#..........
............#...............................................................................#....#...........#..........#.........
................................................##...............................................#..#..........................#..
.................#.......#........................................................................#...............................
..#.........................#......#.............#.......................................#........................................
...............#.............#...........................................................#.....#..................................
.........#...............................................................................#...............................#........
.........................................#...................#.................#.........##........#.........#....................
............#..........#.....#................................................................#...##............................#.
........#...#....#..............................................#..............#........................#.........................
..#.....................................................................................................................#.........
.#....#.............................^................#..#...................#.........................#...........................
..........................................................................#.........#....#......#.................................
.........#................................#.#........................#.................#...................................#......
.............................................#.##............................................................#......#..#.........#
..........#............#...........#..#......#..........#.........................................................................
......................#....................................#....#.............##....#.............................................
......................#...#............#.......................................................................................#..
.##.................#.......................#...............#.............#......#..................................#.....#.#.....
....................#........#.......................#....................................#.......#...#.......#.......#......#....
.............................................................#.......................#..........................#.....#...........
...#.................#.......................................................#.......##...........#.......#.......................
...............##.........................#.........................................................#.....#.......#...............
.......................#.......................#.........#..............#....................#..........#........................#
...................................##..........#..........................................................#.........#.............
..................#...............................#...................................#.......#.......................#...........
.......................#..#...................................#........................#........#............#....................
...................................#....#............#..................#........................................#..........#.....
.............#...#...#......#.............##...............................................#..........................#....#......
....................#..........................................#....#......................................................#......
............#.........#...............#..#.....................................................................#.#................
.......................#..#..............................................................#.....#........#..#..................#...
.............#..#..............................#.....#.................#.............#.......................#................#...
...............#......#...........#............#.........#......................................#.................................
............................#.....#.........#.....#..#...........#................................................................
....#.......#.................#..............................................#.......#.#.............................#...#..#.....
..................................................#.#......#............................................................#.........
..................................#............#........................#.......#.........#...#...............#...................
............##....#.#......#..............................................................................#..............#........
.....#..........................................#.........................................................#........##.............
............#.....................#..#.#..............#........#......#.............................#....#...#....................
.......................#...........................................................................#..............................
......#.........................................#........#............#..#..............................#.#.......................
#.#......#..#...............#...........#....#.................................................#..................................
.........#...........#............................#..............#......................#.......................................#.
...#............#..................................#..............#............................#.........................#........
...##..#.....................................................................................#...........................#........
...............#......#.........#................................#...#............#....................#..........................
..........................#...........................#..............................................#................#....#......
.........#........#.#...........................................................................#..#..............................
.................#..............#........................................................................#.................#......
...#.........#.#.........#.#...........................................#........#........#.........#..............................
..........#............................................................#..........#.....#.........................................
..................................#.....#...........##........#......#..........#..........................#......................
...........................#....#.............#............................................................#......................
.............#.......#...................................#.....#............................................................##....
............#..............##.............#.....#...............#..........#........................#.........................#...
..##.....................................................................................................#........................
.............#.#...........#...................#....#...#......#................##................................................
.................#.#............#........................#.......##..#.........##.................................................
......................#.#...#................................................................#...............#.....#...........#..
#.................#..........................#.............................##.....#...........................................#...
..............#.........#.................#................................................................................#......
....#.#............#.......#.......................#.....#.......................#....................#.....#.............#.......
......................#..#....#.........................................#.#............##............#............................
.........#.#...#...#........................................#...............................................#....................#
.......................#...................#.............................................................#.......................#
................#............................#........#..........#.......................##....#..................................
.#...................#......................#.......................................#............................#................
..#..##.......#......#..........#..#..................................................#...........................................
..............#..........#...........................................#.........##.................................................
....#..............................#.........#...#.................#......#.#.......#.............................................
#.................................#........#.....................................#...##...................#..#...........#........
.......#.....#.............................................#..................#...................#...........#..#........#.......
.......................#................#.............#.#.........#..............................................................#
......................................................#....................#..........#................................#..........
#...............#...#.............#.................#.................................................#...........................
..................................................................#.........................#......#.........#............##......
#.................#........#.......#...#....................................#.#...................................................
.....................................#...#....#.........#................#.........................................#...#..........
............#............................#.............#.#........................................................................
......................................#.................................................#...............#.......#.................
.#.#..........#........#.......................#..................................................#....................#..........
....#...............................................................#...........#............#.......................#............
....#.......#.#..#...................#.........#..................................#....................................#..........
..............................................#...................................##.......#......................................
#...#.#............#...............................#.........#...........#..........#............................................#
..#...........#..#..........#.......................#..........##.................................................................
...#.....#..................................#................................................#....................................
"""


def parse(data: str):
    board = np.array(
        [
            [2 if c == "^" else (1 if c == "#" else 0) for c in line]
            for line in data.strip().split("\n")
        ]
    )
    pos = np.where(board == 2)
    row, col = pos[0][0], pos[1][0]
    board[row, col] = 0
    initial_state = (row, col, -1, 0)
    return board, initial_state


def turn_vector_90_deg(vector: tuple[int, int]):
    if vector == (-1, 0):
        return (0, 1)
    elif vector == (0, 1):
        return (1, 0)
    elif vector == (1, 0):
        return (0, -1)
    elif vector == (0, -1):
        return (-1, 0)
    raise ValueError(f"Invalid vector: {vector}")


def move(
    board: np.ndarray,
    state: tuple[int, int, int, int],
    states_on_path: set = None,
    simulating: bool = False,
    trapping_obstacle_positions: set = None,
    checked_obstacle_positions: set = None,
) -> tuple[bool, set, set]:
    if states_on_path is None:
        states_on_path = set()
    if trapping_obstacle_positions is None:
        trapping_obstacle_positions = set()
    if checked_obstacle_positions is None:
        checked_obstacle_positions = set()

    row, col, d_row, d_col = state

    # -- check for loop --
    if state in states_on_path:
        return (True, None, None)
    states_on_path.add(state)

    # -- check for edge of board --
    if (
        row + d_row < 0
        or row + d_row >= board.shape[0]
        or col + d_col < 0
        or col + d_col >= board.shape[1]
    ):
        # next step would be out of bounds
        return (False, trapping_obstacle_positions, states_on_path)

    blocked = board[row + d_row, col + d_col]

    # -- check outcome of placing obstacle --
    if not simulating and not blocked:
        # check if obstacle position has already been checked from another direction
        if (row + d_row, col + d_col) not in checked_obstacle_positions:
            # check outcome of placing an obstacle in front
            board_with_obstacle = copy(board)
            board_with_obstacle[row + d_row, col + d_col] = 1
            new_dir = turn_vector_90_deg((d_row, d_col))
            loop, _, _ = move(
                board_with_obstacle,
                (row, col, new_dir[0], new_dir[1]),
                copy(states_on_path),
                simulating=True,
            )
            if loop:
                trapping_obstacle_positions.add((row + d_row, col + d_col))
            # else: placing the obstacle does not trap the guard in a loop
            checked_obstacle_positions.add((row + d_row, col + d_col))

    # -- move --
    if blocked:
        # turn 90 degrees to the right
        new_dir = turn_vector_90_deg((d_row, d_col))
        return move(
            board,
            (row, col, new_dir[0], new_dir[1]),
            states_on_path,
            simulating,
            trapping_obstacle_positions,
            checked_obstacle_positions,
        )
    # move forward
    return move(
        board,
        (row + d_row, col + d_col, d_row, d_col),
        states_on_path,
        simulating,
        trapping_obstacle_positions,
        checked_obstacle_positions,
    )


def solve(data: str):
    board, initial_state = parse(data)
    print(initial_state)
    loop, obstacle_positions, positions_on_path = move(board, initial_state)
    if loop:
        print(obstacle_positions)
        raise ValueError("Board leads to infinite loop")

    # reduce the set 'states_on_path' from (x,y,d_row,d_col) to (x,y)
    positions_on_path = {(x, y) for x, y, _, _ in positions_on_path}

    print("Number of states on path:", len(positions_on_path))
    print("Number of obstacle positions:", len(obstacle_positions))
    return len(positions_on_path), len(obstacle_positions)


def solve1(data: str):
    return solve(data)[0]


def solve2(data: str):
    return solve(data)[1]


testData = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


class Tests(unittest.TestCase):
    def test_solve1(self):
        self.assertEqual(solve1(testData), 41)
        self.assertEqual(solve1(data), 4988)

    def test_solve2(self):
        self.assertEqual(solve2(testData), 6)
        self.assertEqual(solve2(data), 1697)


if __name__ == "__main__":
    print(solve1(data))
    print(solve2(data))

    unittest.main()