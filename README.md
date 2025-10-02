# Graphical Sequence Checker

## 📘 Overview

This program checks whether a given integer sequence is **graphical** (i.e., can be represented as the degree sequence of a simple graph) using the **Havel–Hakimi algorithm**.
If the sequence is graphical, the program generates and visualizes a random graph that satisfies the degree sequence using **NetworkX**.

## 🏗️ Tech Stack

* **Python 3**
* **Libraries:**

  * [NetworkX](https://networkx.org/) – for graph generation and visualization
  * [Matplotlib](https://matplotlib.org/) – for drawing graphs

## ⚙️ How It Works

1. The algorithm takes a sequence of integers.
2. It repeatedly reduces the sequence based on the first element until:

   * All elements are reduced to zero → sequence is graphical.
   * A negative number appears → sequence is not graphical.
3. If the sequence is graphical:

   * A random graph with the given degree sequence is generated.
   * The graph is displayed using a circular layout.

## 📊 Example

### Input Sequences:

```python
seq1 = [5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3]
seq2 = [6, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1]
```

### Output:

* `seq1` → Graphical → Graph is drawn.
* `seq2` → Not graphical.

## ▶️ Usage

Run the program:

```bash
python graphical_sequence_checker.py
```

Modify `seq1` or `seq2` to test other sequences.

---
