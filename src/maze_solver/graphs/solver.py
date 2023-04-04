# graphs/solver.py

import networkx as nx

from maze_solver.graphs.converter import make_graph
from maze_solver.models.maze import Maze
from maze_solver.models.solution import Solution


def solve(maze: Maze) -> Solution | None:
    """
    This function solve takes a maze object of type Maze as input and attempts to find the shortest path from its entrance to its exit. If a solution is found, it returns a Solution object with the shortest path as a tuple of squares; if no solution is found or an error occurs, it returns None.
    """
    try:
        return Solution(
            squares=tuple(
                nx.shortest_path(
                    make_graph(maze),
                    source=maze.entrance,
                    target=maze.exit,
                    weight="weight",
                )
            )
        )
    except nx.NetworkXException:
        return None


def solve_all(maze: Maze) -> list[Solution]:
    try:
        return [
            Solution(squares=tuple(path))
            for path in nx.all_shortest_paths(
                make_graph(maze),
                source=maze.entrance,
                target=maze.exit,
                weight="weight",
            )
        ]
    except nx.NetworkXException:
        return []
