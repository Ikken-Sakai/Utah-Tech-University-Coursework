# CS2810 - Computer Organization and Architecture
# CS2810 - コンピュータ構成とアーキテクチャ

> 📚 Course page: [Utah Tech University - CS2810](https://www.cs.utahtech.edu/)

## 📋 Course Overview / 科目概要

| Item / 項目 | Details / 詳細 |
|-------------|----------------|
| Course / 科目名 | CS2810 - Computer Organization and Architecture |
| Credits / 単位 | 3 credits |
| Prerequisites / 前提科目 | CS1410, CS2100 (Discrete Math) |
| Languages / 使用言語 | C, RISC-V Assembly |

## 🎯 Course Description / 科目説明

### English
This course provides a comprehensive understanding of computer organization and architecture at the hardware level. Students learn low-level programming in C, including memory management, pointers, and system calls. The course also covers RISC-V assembly language programming, teaching how high-level code translates to machine instructions. Topics include CPU architecture, instruction sets, memory hierarchy, and the relationship between hardware and software.

### 日本語
この科目では、ハードウェアレベルでのコンピュータ構成とアーキテクチャについて包括的に学びます。メモリ管理、ポインタ、システムコールを含むC言語での低レベルプログラミングを学習します。また、RISC-Vアセンブリ言語プログラミングも扱い、高レベルのコードが機械命令にどのように変換されるかを学びます。CPU アーキテクチャ、命令セット、メモリ階層、ハードウェアとソフトウェアの関係などのトピックを扱います。

## 📚 Learning Objectives / 学習目標

### English
- Understand computer architecture at the hardware level
- Write efficient C programs with proper memory management
- Use pointers and understand memory allocation
- Program in RISC-V assembly language
- Understand how high-level code compiles to machine code
- Analyze program performance at the instruction level

### 日本語
- ハードウェアレベルでコンピュータアーキテクチャを理解する
- 適切なメモリ管理を持つ効率的なCプログラムを書く
- ポインタを使用し、メモリ割り当てを理解する
- RISC-Vアセンブリ言語でプログラミングする
- 高レベルコードが機械語にコンパイルされる仕組みを理解する
- 命令レベルでプログラムの性能を分析する

## 📂 Directory Structure / ディレクトリ構造

```
CS2810/
├── c-programming/      # C language assignments / C言語課題
│   ├── c-hello-world/  # Basic I/O / 基本入出力
│   ├── c-calculator/   # String parsing with sscanf / sscanfによる文字列解析
│   ├── c-diamond/      # Loop patterns / ループパターン
│   ├── c-difference-of-squares/  # Mathematical functions / 数学関数
│   ├── c-hamming/      # Bit operations / ビット演算
│   ├── c-sieve/        # Sieve of Eratosthenes / エラトステネスの篩
│   ├── c-maze-solver/  # 2D array algorithms / 2次元配列アルゴリズム
│   ├── c-wordle/       # String processing / 文字列処理
│   └── c-midterm/      # Midterm projects / 中間課題
└── risc-v-assembly/    # RISC-V assembly assignments / RISC-Vアセンブリ課題
    ├── rv32-stoi/      # String to integer / 文字列から整数への変換
    ├── rv32-array-max/ # Find max in array / 配列の最大値探索
    ├── rv32-array-sum/ # Array summation / 配列の合計
    ├── rv32-count-jumps/ # Control flow / 制御フロー
    └── sudoku/         # Sudoku solver / 数独ソルバー
```

---

## 🔧 C Programming Projects / Cプログラミングプロジェクト

### Basic Projects / 基礎プロジェクト

| Project | Description / 説明 | Key Concepts / 主要概念 |
|---------|---------------------|-------------------------|
| [c-hello-world](./c-programming/c-hello-world/) | Hello World program / Hello Worldプログラム | Basic I/O, compilation / 基本I/O、コンパイル |
| [c-diamond](./c-programming/c-diamond/) | Diamond pattern printer / ダイヤモンドパターン出力 | Nested loops / ネストされたループ |
| [c-difference-of-squares](./c-programming/c-difference-of-squares/) | Sum of squares calculation / 平方和の計算 | Functions, math / 関数、数学 |

### Intermediate Projects / 中級プロジェクト

| Project | Description / 説明 | Key Concepts / 主要概念 |
|---------|---------------------|-------------------------|
| [c-calculator](./c-programming/c-calculator/) | Text-based calculator / テキストベース電卓 | `sscanf`, string parsing / 文字列解析 |
| [c-hamming](./c-programming/c-hamming/) | Hamming distance calculator / ハミング距離計算 | Bit operations, XOR / ビット演算 |
| [c-sieve](./c-programming/c-sieve/) | Prime number finder / 素数探索 | Sieve of Eratosthenes / エラトステネスの篩 |

### Advanced Projects / 上級プロジェクト

| Project | Description / 説明 | Key Concepts / 主要概念 |
|---------|---------------------|-------------------------|
| [c-maze-solver](./c-programming/c-maze-solver/) | Maze solving algorithm / 迷路解決アルゴリズム | 2D arrays, cellular logic / 2次元配列、セルラーロジック |
| [c-wordle](./c-programming/c-wordle/) | Wordle game implementation / Wordleゲーム実装 | String processing, file I/O / 文字列処理、ファイルI/O |

---

## 🖥️ RISC-V Assembly Projects / RISC-Vアセンブリプロジェクト

| Project | Description / 説明 | Key Concepts / 主要概念 |
|---------|---------------------|-------------------------|
| [rv32-stoi](./risc-v-assembly/rv32-stoi/) | String to integer conversion / 文字列→整数変換 | ASCII, loops / ASCII、ループ |
| [rv32-array-max](./risc-v-assembly/rv32-array-max/) | Find maximum value in array / 配列の最大値探索 | Array indexing, comparisons / 配列インデックス、比較 |
| [rv32-array-sum](./risc-v-assembly/rv32-array-sum/) | Sum array elements / 配列要素の合計 | Loops, accumulator / ループ、アキュムレータ |
| [rv32-count-jumps](./risc-v-assembly/rv32-count-jumps/) | Count jump instructions / ジャンプ命令カウント | Control flow analysis / 制御フロー分析 |
| [sudoku](./risc-v-assembly/sudoku/) | Sudoku solver in assembly / アセンブリで数独ソルバー | Complex algorithms in ASM / 複雑なアルゴリズム |

---

## 🔨 Building & Running / ビルドと実行

### C Projects / Cプロジェクト

Each C project includes a Makefile / 各CプロジェクトにはMakefileが含まれています:

```bash
cd CS2810/c-programming/c-calculator
make        # Build and run tests / ビルドとテスト実行
make a.out  # Build only / ビルドのみ
./a.out     # Run interactively / 対話的に実行
```

### RISC-V Projects / RISC-Vプロジェクト

Requires RISC-V toolchain / RISC-Vツールチェーンが必要:

```bash
cd CS2810/risc-v-assembly/rv32-stoi
make        # Assemble and test / アセンブルとテスト
```

## 🛠️ Technologies / 使用技術

- **C Language / C言語**: GCC, Make, GDB
- **RISC-V Assembly / RISC-Vアセンブリ**: 32-bit RISC-V ISA
- **Tools / ツール**: Valgrind (memory debugging / メモリデバッグ), GDB (debugging / デバッグ)
