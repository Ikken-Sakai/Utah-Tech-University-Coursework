# Utah Tech University - Computer Science Coursework

[![University](https://img.shields.io/badge/University-Utah%20Tech-red)](https://utahtech.edu/)
[![Department](https://img.shields.io/badge/Department-Computer%20Science-blue)](https://utahtech.edu/)

This repository contains coursework and projects from my Computer Science studies at Utah Tech University (formerly Dixie State University).

## 📚 Courses

### [CS1410 - Introduction to Computer Science](./CS1410/)

Fundamentals of programming with Python.

| Project | Description |
|---------|-------------|
| `caloric_balance.py` | Caloric balance calculator |
| `DNA.py` | DNA sequence analysis |
| `Create_Data_Files.py` | File I/O operations |

**Skills**: Python basics, File I/O, Functions

---

### [CS2420 - Data Structures & Algorithms](./CS2420/)

Implementation of fundamental data structures and algorithms in Python.

| Category | Projects |
|----------|----------|
| **Trees** | Binary Search Tree (`BST.py`) |
| **Lists** | Linked Lists (`linkedlists.py`) |
| **Hash** | Hash Table (`hashtable.py`) |
| **Heap** | Min/Max Heap (`heap.py`) |
| **Stack/Queue** | Stack & Queue implementations |
| **Graphs** | Graph traversal, Dijkstra's algorithm |
| **Sorting** | Bubble, Selection, Merge, Quick Sort |

**Skills**: Algorithm complexity, OOP, Problem solving

---

### [CS2810 - Computer Organization & Architecture](./CS2810/)

Low-level programming with C and RISC-V assembly.

#### C Programming

| Project | Description | Skills |
|---------|-------------|--------|
| `c-hello-world` | Hello World | Basic I/O |
| `c-calculator` | Text calculator | `sscanf`, parsing |
| `c-diamond` | Diamond pattern | Loops |
| `c-hamming` | Hamming distance | Bit operations |
| `c-sieve` | Prime finder | Sieve algorithm |
| `c-maze-solver` | Maze solver | 2D arrays, cellular logic |
| `c-wordle` | Wordle clone | String processing |

#### RISC-V Assembly

| Project | Description |
|---------|-------------|
| `rv32-stoi` | String to integer conversion |
| `rv32-array-max` | Find maximum in array |
| `rv32-array-sum` | Array summation |
| `rv32-count-jumps` | Control flow counting |
| `sudoku` | Sudoku solver in assembly |

**Skills**: Memory management, CPU architecture, Assembly programming

---

## 📂 Repository Structure

```
Utah-Tech-University-Coursework/
├── CS1410/                     # Intro to CS (Python)
│   ├── README.md
│   ├── caloric_balance.py
│   ├── DNA.py
│   └── ...
├── CS2420/                     # Data Structures (Python)
│   ├── README.md
│   ├── BST.py
│   ├── graph-dijkstra.py
│   └── ...
└── CS2810/                     # Computer Architecture
    ├── README.md
    ├── c-programming/          # C assignments
    │   ├── c-calculator/
    │   ├── c-maze-solver/
    │   └── ...
    └── risc-v-assembly/        # RISC-V assignments
        ├── rv32-stoi/
        ├── sudoku/
        └── ...
```

## 🛠️ Technologies Used

| Language | Tools | Topics |
|----------|-------|--------|
| **Python** | Python 3.x | OOP, Data Structures, Algorithms |
| **C** | GCC, Make, GDB | Memory management, Systems programming |
| **RISC-V** | RISC-V toolchain | Assembly, CPU architecture |

## 🔧 Building & Running

### Python Projects
```bash
cd CS2420
python3 BST.py
```

### C Projects
```bash
cd CS2810/c-programming/c-calculator
make        # Build and test
./a.out     # Run
```

### RISC-V Projects
```bash
cd CS2810/risc-v-assembly/rv32-stoi
make        # Assemble and test
```

## 👤 Author

**Ikken Sakai (坂井 壱謙)**
- Former Utah Tech University Computer Science Student
- Currently: 東京国際工科専門職大学 工科学部 情報工学科 AI戦略コース
- GitHub: [@Ikken-Sakai](https://github.com/Ikken-Sakai)
