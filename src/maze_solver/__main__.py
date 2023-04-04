# __main__.py

import argparse
import pathlib

from maze_solver.graphs.solver import solve
from maze_solver.models.maze import Maze
from maze_solver.view.renderer import SVGRenderer


def main() -> None:
    maze = Maze.load(parse_path())
    solution = solve(maze)
    if solution:
        renderer = SVGRenderer()
        # for solution in solutions:
        renderer.render(maze, solution).preview()
    else:
        print("No solution found")


def parse_path() -> pathlib.Path:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=pathlib.Path)
    return parser.parse_args().path


if __name__ == "__main__":
    main()
