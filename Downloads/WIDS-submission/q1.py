# pyright: ignore[reportMissingImports]

from pysat.formula import CNF
from pysat.solvers import Solver
from typing import List

def solve_sudoku(grid: List[List[int]]) -> List[List[int]]:
    cnf = CNF()

    # variable mapping: (i,j,n) -> unique three digit int (I could assign a 3 element list too)
    def var(i, j, n):
        return i * 100 + j * 10 + n

    # already filled numbers
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                cnf.append([var(i+1, j+1, grid[i][j])])

    # EACH CELL: minimum one number
    for i in range(1, 10):
        for j in range(1, 10):
            cnf.append([var(i, j, n) for n in range(1, 10)])

    # EACH CELL: at max one number
    for i in range(1, 10):
        for j in range(1, 10):
            for n in range(1, 10):
                for m in range(n+1, 10):
                    cnf.append([-var(i, j, n), -var(i, j, m)])

    # ROW CONSTRAINTS
    for i in range(1, 10):
        for n in range(1, 10):
            for j in range(1, 10):
                for k in range(j+1, 10):
                    cnf.append([-var(i, j, n), -var(i, k, n)])

    # COLUMN CONSTRAINTS
    for j in range(1, 10):
        for n in range(1, 10):
            for i in range(1, 10):
                for k in range(i+1, 10):
                    cnf.append([-var(i, j, n), -var(k, j, n)])

    # 3×3 BLOCK CONSTRAINTS
    for br in [1, 4, 7]:
        for bc in [1, 4, 7]:
            cells = [(br+r, bc+c) for r in range(3) for c in range(3)]
            for n in range(1, 10):
                for a in range(len(cells)):
                    for b in range(a+1, len(cells)):
                        r1, c1 = cells[a]
                        r2, c2 = cells[b]
                        cnf.append([-var(r1, c1, n), -var(r2, c2, n)])

    # SOLVE sudoku
    solver = Solver(name="glucose3")
    solver.append_formula(cnf.clauses)

    if not solver.solve():
        # UNSAT edge case safety
        return [[0]*9 for _ in range(9)]

    model = solver.get_model()

    # MODEL → GRID
    solved = [[0]*9 for _ in range(9)]
    for lit in model:
        if lit > 0:
            i = lit // 100
            j = (lit // 10) % 10
            n = lit % 10
            if 1 <= i <= 9 and 1 <= j <= 9 and 1 <= n <= 9:
                solved[i-1][j-1] = n

    return solved