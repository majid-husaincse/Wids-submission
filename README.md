# WIDS Submission

This repository contains my WIDS project submission, organized as individual
Python files corresponding to each question and algorithm implemented.

The commit history of this repository may appear inconsistent. This is due to
multiple uploads. Please ignore
the commit history and focus only on the final versions of the code files present
in the repository.

In addition to the problem-specific solvers, I have included basic implementations
of the DPLL and CDCL algorithms that I developed earlier. These implementations
were created before working on the Sudoku and Sokoban solvers and were later used
as references while building them.

## Theory and Resources Used

The following resources were used to understand the theory and implementation
details required for this project:

- **CS Logic Course Slides (Lectures 1–10)**  
  Used to understand propositional logic, SAT solvers, and the DPLL algorithm.

- **Lectures by Prof. Anshuman Gupta**  
  Used to gain a clearer understanding of DPLL, its optimizations, and the idea
  behind conflict-driven clause learning (CDCL).

- **freeCodeCamp (Python)**  
  Used for learning and revising Python at a basic level.

No external SAT solver libraries were used. All logic was implemented manually to
gain better conceptual clarity.

---

## Repository Structure

The repository contains the following files:

- `q1.py`  
  SAT solver for Sudoku

- `q2.py`  
  SAT solver for Sokoban

- `dpll.py`  
  Basic implementation of the DPLL algorithm

- `cdcl.py`  
  Basic implementation of the CDCL algorithm

Each file is self-contained and can be accessed directly. The problem-specific
solvers were written after implementing the standalone DPLL and CDCL algorithms.

---

## How the Project Works

The overall workflow of the project is as follows:

1. Constraint problems such as Sudoku and Sokoban are encoded into propositional
   logic formulas.
2. These formulas are represented in CNF (Conjunctive Normal Form).
3. A SAT solver based on DPLL or CDCL is used to determine satisfiability.
4. A satisfying assignment, if found, is interpreted back as a valid solution to
   the original problem.

---

## Learnings and Takeaways

Through this project, I gained a deeper understanding of:
- SAT solvers and propositional logic
- DPLL and CDCL algorithms
- Encoding real-world constraints as logical formulas
- Writing structured and modular Python code

This project helped connect theoretical concepts from logic courses to practical
problem-solving .

---

## Usefulness

SAT solvers provide a general framework for solving a wide range of constraint
satisfaction problems. And they are fun ! :P
