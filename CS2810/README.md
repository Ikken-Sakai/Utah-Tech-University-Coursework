# CS2810 - Computer Organization & Architecture

## 📋 Course Overview

| Item | Details |
|------|---------|
| Course | CS2810 - Computer Organization and Architecture |
| Languages | C, RISC-V Assembly |
| Topics | Low-level programming, Memory management, CPU architecture |

## 🎯 Learning Objectives

- Understand computer architecture at the hardware level
- Write efficient C programs with memory management
- Program in RISC-V assembly language
- Understand how high-level code translates to machine instructions

## 📂 Directory Structure

```
CS2810/
├── c-programming/      # C language assignments
│   ├── c-hello-world/  # Basic I/O
│   ├── c-calculator/   # String parsing with sscanf
│   ├── c-diamond/      # Loop patterns
│   ├── c-difference-of-squares/  # Mathematical functions
│   ├── c-hamming/      # Bit operations
│   ├── c-sieve/        # Sieve of Eratosthenes
│   ├── c-maze-solver/  # 2D array algorithms
│   ├── c-wordle/       # String processing
│   └── c-midterm/      # Midterm projects
└── risc-v-assembly/    # RISC-V assembly assignments
    ├── rv32-stoi/      # String to integer
    ├── rv32-array-max/ # Find max in array
    ├── rv32-array-sum/ # Array summation
    ├── rv32-count-jumps/ # Control flow
    └── sudoku/         # Sudoku solver
```

---

## 🔧 C Programming Projects

### Basic Projects

| Project | Description | Key Concepts |
|---------|-------------|--------------|
| [c-hello-world](./c-programming/c-hello-world/) | Hello World program | Basic I/O, compilation |
| [c-diamond](./c-programming/c-diamond/) | Diamond pattern printer | Nested loops, patterns |
| [c-difference-of-squares](./c-programming/c-difference-of-squares/) | Sum of squares calculation | Functions, math |

### Intermediate Projects

| Project | Description | Key Concepts |
|---------|-------------|--------------|
| [c-calculator](./c-programming/c-calculator/) | Text-based calculator | `sscanf`, string parsing |
| [c-hamming](./c-programming/c-hamming/) | Hamming distance calculator | Bit operations, XOR |
| [c-sieve](./c-programming/c-sieve/) | Prime number finder | Sieve of Eratosthenes, arrays |

### Advanced Projects

| Project | Description | Key Concepts |
|---------|-------------|--------------|
| [c-maze-solver](./c-programming/c-maze-solver/) | Maze solving algorithm | 2D arrays, cellular logic |
| [c-wordle](./c-programming/c-wordle/) | Wordle game implementation | String processing, file I/O |
| [c-midterm](./c-programming/c-midterm/) | Midterm exam projects | Various |

---

## 🖥️ RISC-V Assembly Projects

| Project | Description | Key Concepts |
|---------|-------------|--------------|
| [rv32-stoi](./risc-v-assembly/rv32-stoi/) | String to integer conversion | ASCII, loops |
| [rv32-array-max](./risc-v-assembly/rv32-array-max/) | Find maximum value in array | Array indexing, comparisons |
| [rv32-array-sum](./risc-v-assembly/rv32-array-sum/) | Sum array elements | Loops, accumulator pattern |
| [rv32-count-jumps](./risc-v-assembly/rv32-count-jumps/) | Count jump instructions | Control flow analysis |
| [sudoku](./risc-v-assembly/sudoku/) | Sudoku solver in assembly | Complex algorithms in ASM |

---

## 🔨 Building & Running

### C Projects

Each C project includes a Makefile:

```bash
cd CS2810/c-programming/c-calculator
make        # Build and run tests
make a.out  # Build only
./a.out     # Run interactively
```

### RISC-V Projects

Requires RISC-V toolchain:

```bash
cd CS2810/risc-v-assembly/rv32-stoi
make        # Assemble and test
```

## 🛠️ Technologies

- **C Language**: GCC, Make, GDB
- **RISC-V Assembly**: 32-bit RISC-V ISA
- **Tools**: Valgrind (memory debugging), GDB (debugging)

