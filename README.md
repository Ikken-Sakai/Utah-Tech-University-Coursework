# Utah Tech University - Computer Science Coursework
# ユタ工科大学 - コンピュータサイエンス課題

[![University](https://img.shields.io/badge/University-Utah%20Tech-red)](https://utahtech.edu/)
[![Department](https://img.shields.io/badge/Department-Computer%20Science-blue)](https://www.cs.utahtech.edu/)

This repository contains coursework and projects from my Computer Science studies at Utah Tech University (formerly Dixie State University).

このリポジトリには、Utah Tech University（旧 Dixie State University）でのコンピュータサイエンス学習における課題とプロジェクトを収録しています。

> 📚 Department page: [Utah Tech University - Department of Computing](https://www.cs.utahtech.edu/)

---

## 📚 Courses / 履修科目

### [CS1410 - Object-Oriented Programming](./CS1410/)
### CS1410 - オブジェクト指向プログラミング

**English**: Introduction to object-oriented programming concepts using Python. Covers classes, inheritance, polymorphism, and file I/O operations.

**日本語**: Pythonを使用したオブジェクト指向プログラミングの入門。クラス、継承、ポリモーフィズム、ファイルI/O操作を学習。

| Project / プロジェクト | Description / 説明 |
|------------------------|---------------------|
| `caloric_balance.py` | Caloric balance calculator / カロリーバランス計算 |
| `DNA.py` | DNA sequence analysis / DNA配列分析 |
| `Create_Data_Files.py` | File I/O operations / ファイルI/O操作 |

**Skills / 習得スキル**: Python basics, OOP, File I/O

---

### [CS2420 - Data Structures and Algorithms](./CS2420/)
### CS2420 - データ構造とアルゴリズム

**English**: Implementation of fundamental data structures and algorithms. Covers linked lists, trees, graphs, hash tables, and sorting algorithms with Big-O analysis.

**日本語**: 基本的なデータ構造とアルゴリズムの実装。連結リスト、木構造、グラフ、ハッシュテーブル、ソートアルゴリズムをBig-O分析とともに学習。

| Category / カテゴリ | Projects / プロジェクト |
|---------------------|-------------------------|
| **Trees / 木構造** | Binary Search Tree (`BST.py`) / 二分探索木 |
| **Lists / リスト** | Linked Lists (`linkedlists.py`) / 連結リスト |
| **Hash / ハッシュ** | Hash Table (`hashtable.py`) / ハッシュテーブル |
| **Heap / ヒープ** | Min/Max Heap (`heap.py`) / 最小・最大ヒープ |
| **Stack/Queue** | Stack & Queue implementations / スタック・キュー実装 |
| **Graphs / グラフ** | Graph traversal, Dijkstra / グラフ走査、ダイクストラ法 |
| **Sorting / ソート** | Bubble, Selection, Merge, Quick Sort / 各種ソート |

**Skills / 習得スキル**: Algorithm complexity (Big-O), OOP, Problem solving

---

### [CS2810 - Computer Organization and Architecture](./CS2810/)
### CS2810 - コンピュータ構成とアーキテクチャ

**English**: Low-level programming with C and RISC-V assembly. Covers memory management, pointers, CPU architecture, and how high-level code translates to machine instructions.

**日本語**: C言語とRISC-Vアセンブリによる低レベルプログラミング。メモリ管理、ポインタ、CPUアーキテクチャ、高レベルコードから機械命令への変換を学習。

#### C Programming / Cプログラミング

| Project / プロジェクト | Description / 説明 | Skills / スキル |
|------------------------|---------------------|-----------------|
| `c-hello-world` | Hello World | Basic I/O / 基本I/O |
| `c-calculator` | Text calculator / テキスト電卓 | `sscanf`, parsing / 文字列解析 |
| `c-diamond` | Diamond pattern / ダイヤモンドパターン | Loops / ループ |
| `c-hamming` | Hamming distance / ハミング距離 | Bit operations / ビット演算 |
| `c-sieve` | Prime finder / 素数探索 | Sieve algorithm / 篩アルゴリズム |
| `c-maze-solver` | Maze solver / 迷路ソルバー | 2D arrays, cellular logic |
| `c-wordle` | Wordle clone | String processing / 文字列処理 |

#### RISC-V Assembly / RISC-Vアセンブリ

| Project / プロジェクト | Description / 説明 |
|------------------------|---------------------|
| `rv32-stoi` | String to integer conversion / 文字列→整数変換 |
| `rv32-array-max` | Find maximum in array / 配列の最大値 |
| `rv32-array-sum` | Array summation / 配列の合計 |
| `rv32-count-jumps` | Control flow counting / 制御フローカウント |
| `sudoku` | Sudoku solver in assembly / アセンブリで数独ソルバー |

**Skills / 習得スキル**: Memory management, CPU architecture, Assembly programming

---

## 📂 Repository Structure / リポジトリ構造

```
Utah-Tech-University-Coursework/
├── CS1410/                     # Object-Oriented Programming (Python)
│   │                           # オブジェクト指向プログラミング
│   ├── README.md
│   ├── caloric_balance.py
│   ├── DNA.py
│   └── ...
├── CS2420/                     # Data Structures & Algorithms (Python)
│   │                           # データ構造とアルゴリズム
│   ├── README.md
│   ├── BST.py
│   ├── graph-dijkstra.py
│   └── ...
└── CS2810/                     # Computer Architecture (C, RISC-V)
    │                           # コンピュータアーキテクチャ
    ├── README.md
    ├── c-programming/          # C assignments / C言語課題
    │   ├── c-calculator/
    │   ├── c-maze-solver/
    │   └── ...
    └── risc-v-assembly/        # RISC-V assignments / RISC-V課題
        ├── rv32-stoi/
        ├── sudoku/
        └── ...
```

## 🛠️ Technologies Used / 使用技術

| Language / 言語 | Tools / ツール | Topics / トピック |
|-----------------|----------------|-------------------|
| **Python** | Python 3.x | OOP, Data Structures, Algorithms |
| **C** | GCC, Make, GDB | Memory management, Systems programming |
| **RISC-V** | RISC-V toolchain | Assembly, CPU architecture |

## 🔧 Building & Running / ビルドと実行

### Python Projects / Pythonプロジェクト
```bash
cd CS2420
python3 BST.py
```

### C Projects / Cプロジェクト
```bash
cd CS2810/c-programming/c-calculator
make        # Build and test / ビルドとテスト
./a.out     # Run / 実行
```

### RISC-V Projects / RISC-Vプロジェクト
```bash
cd CS2810/risc-v-assembly/rv32-stoi
make        # Assemble and test / アセンブルとテスト
```

## 👤 Author / 著者

**Ikken Sakai (坂井 壱謙)**
- Former Utah Tech University Computer Science Student
- Currently: 東京国際工科専門職大学 工科学部 情報工学科 AI戦略コース
- GitHub: [@Ikken-Sakai](https://github.com/Ikken-Sakai)
