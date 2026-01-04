def dpll(cnf,assignment={}):
    def simplify(cnf,var,val):
        new=[]
        for clause in cnf:
            if (var if val else "~" + var) in clause:
                continue
            new_clause=[l for l in clause if l!=("~" + var if val else var)]
            new.append(new_clause)
        return new
    
    for clause in cnf:
        if len(clause) == 1:
            lit = clause[0]
            var = lit.strip("~")
            val = not lit.startswith("~")
            return dpll(simplify(cnf, var, val), {**assignment, var: val})
    if cnf==[]:
        answer=[]
        for keys in assignment:
            if assignment[keys]==True:
                answer.append(keys)
        return True, answer
    if [] in cnf:
        return False, "possible hi ni hai"
    
    lit = cnf[0][0]
    var = lit.strip("~")

    sat, sol = dpll(simplify(cnf, var, True), {**assignment, var: True})
    if sat:
        return True, sol
    return dpll(simplify(cnf, var, False), {**assignment, var: False})
            
cnf1 = [
    ["A", "B"],
    ["~A", "C"],
    
]

cnf2 = [
    ["A", "B"],
    ["~A", "C"],
    ["~B"],["~C"]
]
print(dpll(cnf1))
print()
print(dpll(cnf2))
print()

def sudoku_4x4_cnf():
    cnf = []

    def P(i,j,n):
        return f"P({i},{j},{n})"

    # ----- GIVEN CELLS -----
    given = [
        (1,2,2),(1,3,4),
        (2,1,1),(2,4,3),
        (3,1,4),(3,4,2),
        (4,2,1),(4,3,3)
    ]
    for i,j,n in given:
        cnf.append([P(i,j,n)])

    # ----- EACH CELL: at least one -----
    for i in range(1,5):
        for j in range(1,5):
            cnf.append([P(i,j,n) for n in range(1,5)])

    # ----- EACH CELL: at most one -----
    for i in range(1,5):
        for j in range(1,5):
            for n in range(1,5):
                for m in range(n+1,5):
                    cnf.append([f"~{P(i,j,n)}", f"~{P(i,j,m)}"])

    # ----- ROW CONSTRAINTS -----
    for i in range(1,5):
        for n in range(1,5):
            for j in range(1,5):
                for k in range(j+1,5):
                    cnf.append([f"~{P(i,j,n)}", f"~{P(i,k,n)}"])

    # ----- COLUMN CONSTRAINTS -----
    for j in range(1,5):
        for n in range(1,5):
            for i in range(1,5):
                for k in range(i+1,5):
                    cnf.append([f"~{P(i,j,n)}", f"~{P(k,j,n)}"])

    # ----- 2×2 BLOCK CONSTRAINTS -----
    blocks = [
        [(1,1),(1,2),(2,1),(2,2)],
        [(1,3),(1,4),(2,3),(2,4)],
        [(3,1),(3,2),(4,1),(4,2)],
        [(3,3),(3,4),(4,3),(4,4)]
    ]
    for block in blocks:
        for n in range(1,5):
            for i in range(len(block)):
                for j in range(i+1,len(block)):
                    r1,c1 = block[i]
                    r2,c2 = block[j]
                    cnf.append([f"~{P(r1,c1,n)}", f"~{P(r2,c2,n)}"])

    return cnf

cnf = sudoku_4x4_cnf()
print(dpll(cnf))
print()

def sudoku_9x9_cnf():
    cnf = []
    given = [
    (1,1,5),(1,2,3),(1,5,7),
    (2,1,6),(2,4,1),(2,5,9),(2,6,5),
    (3,2,9),(3,3,8),(3,8,6),

    (4,1,8),(4,5,6),(4,9,3),
    (5,1,4),(5,4,8),(5,6,3),(5,9,1),
    (6,1,7),(6,5,2),(6,9,6),

    (7,2,6),(7,7,2),(7,8,8),
    (8,4,4),(8,5,1),(8,6,9),(8,9,5),
    (9,5,8),(9,8,7),(9,9,9)
]

    def P(i,j,n):
        return f"P({i},{j},{n})"

    # ----- GIVEN CELLS -----
    for i,j,n in given:
        cnf.append([P(i,j,n)])

    # ----- EACH CELL: at least one -----
    for i in range(1,10):
        for j in range(1,10):
            cnf.append([P(i,j,n) for n in range(1,10)])

    # ----- EACH CELL: at most one -----
    for i in range(1,10):
        for j in range(1,10):
            for n in range(1,10):
                for m in range(n+1,10):
                    cnf.append([f"~{P(i,j,n)}", f"~{P(i,j,m)}"])

    # ----- ROW CONSTRAINTS -----
    for i in range(1,10):
        for n in range(1,10):
            for j in range(1,10):
                for k in range(j+1,10):
                    cnf.append([f"~{P(i,j,n)}", f"~{P(i,k,n)}"])

    # ----- COLUMN CONSTRAINTS -----
    for j in range(1,10):
        for n in range(1,10):
            for i in range(1,10):
                for k in range(i+1,10):
                    cnf.append([f"~{P(i,j,n)}", f"~{P(k,j,n)}"])

    # ----- 3×3 BLOCK CONSTRAINTS -----
    for br in [1,4,7]:
        for bc in [1,4,7]:
            cells = [(br+r, bc+c) for r in range(3) for c in range(3)]
            for n in range(1,10):
                for i in range(len(cells)):
                    for j in range(i+1, len(cells)):
                        r1,c1 = cells[i]
                        r2,c2 = cells[j]
                        cnf.append([f"~{P(r1,c1,n)}", f"~{P(r2,c2,n)}"])

    return cnf


cnf3=sudoku_9x9_cnf()
print(dpll(cnf3))