"""
Sokoban Solver (Search-based)
----------------------------
This solver uses BFS to find a valid sequence of moves
within T steps that places all boxes on goal positions.

Grid Encoding:
- 'P' = Player
- 'B' = Box
- 'G' = Goal
- '#' = Wall
- '.' = Empty space
"""

from collections import deque

UNSAT = -1

# Directions for movement
DIRS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def solve_sokoban(grid, T):
    """
    DO NOT MODIFY THIS FUNCTION SIGNATURE.

    Args:
        grid (list[list[str]]): Sokoban grid
        T (int): Maximum allowed moves

    Returns:
        list[str] : list of moves if solvable
        -1        : if unsatisfiable
    """
    n = len(grid)
    m = len(grid[0])

    walls = set()
    goals = set()
    boxes = set()
    player = None

    # -------- Parse grid --------
    for i in range(n):
        for j in range(m):
            c = grid[i][j]
            if c == '#':
                walls.add((i, j))
            elif c == 'G':
                goals.add((i, j))
            elif c == 'B':
                boxes.add((i, j))
            elif c == 'P':
                player = (i, j)

    if player is None:
        return UNSAT

    # Trivial cases (obvious ones)
    if not boxes:
        return []

    if boxes.issubset(goals):
        return []

    def in_bounds(x, y):
        return (0 <= x < n) and (0 <= y < m)

    # -------- BFS --------
    start_state = (player, frozenset(boxes))
    q = deque()
    q.append((player, frozenset(boxes), []))
    visited = set([start_state])

    while q:
        (px, py), box_set, path = q.popleft()

        if len(path) > T:
            continue

        # Goal check
        if box_set.issubset(goals):
            return path

        for move, (dx, dy) in DIRS.items():
            nx, ny = px + dx, py + dy

            if not in_bounds(nx, ny):
                continue
            if (nx, ny) in walls:
                continue

            new_boxes = set(box_set)

            # Push box if present
            if (nx, ny) in box_set:
                bx, by = nx + dx, ny + dy
                if not in_bounds(bx, by):
                    continue
                if (bx, by) in walls or (bx, by) in box_set:
                    continue
                new_boxes.remove((nx, ny))
                new_boxes.add((bx, by))

            new_state = ((nx, ny), frozenset(new_boxes))
            if new_state not in visited:
                visited.add(new_state)
                q.append(((nx, ny), frozenset(new_boxes), path + [move]))

    return UNSAT