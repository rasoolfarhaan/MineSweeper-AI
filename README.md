# Minesweeper Final AI

## I. Minimal AI
### I.A. Minimal AI Algorithm
Our minimal AI utilized fundamental rules to determine safe moves in Minesweeper. If it couldn't ascertain a safe move, it selected a random covered tile to uncover. The algorithm employed rules of thumb, iterating through the board to identify uncovered tiles with the same number of covered neighbors and effective labels, marking their neighbors as bombs. It then identified uncovered pieces with an effective label of 1 and at least 1 covered neighbor, uncovering one of their covered neighbors. If no such piece was found, it selected a random covered tile. We implemented a Tile class to represent the board, simplifying tile information retrieval.

### I.B. Minimal AI Performance
| Board Size | Sample Size | Score | Worlds Complete |
|------------|-------------|-------|-----------------|
| 5x5        | 1000        | 1000  | 1000            |
| 8x8        | 1000        | 612   | 1000            |
| 16x16      | 1000        | 497   | 1000            |
| 16x30      | 1000        | 18    | 1000            |
| **Total Summary** | **4000** | **2127** | **4000** |

## II. Final AI
### II.A. Final AI Algorithm
In our final AI, we introduced model checking using the backtracking algorithm from project slides. We computed the c frontier and the v frontier, resulting in dictionaries where keys represent v or c values and values represent C(v) or V(c) respectively. We sorted v values by column and row to expedite solution identification. We used an array as our stack, applying backtracking until all solutions were found. We then tallied solutions to determine the tile with the lowest probability of containing a mine.

### II.B. Final AI Performance
| Board Size | Sample Size | Score (average time per world solved) | Worlds Complete |
|------------|-------------|--------------------------------------|-----------------|
| 5x5        | 1000        | 0.001888796                          | 1000            |
| 8x8        | 1000        | 0.008959721                          | 830             |
| 16x16      | 1000        | 0.145882055                          | 807             |
| 16x30      | 1000        | 0.499876575                          | 353             |
| **Total Summary** | **4000** |                                       | **1990**        |

---
Feel free to enhance this README with additional information or sections as needed.
