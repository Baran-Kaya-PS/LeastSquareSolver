# LeastSquareSolver

Goal: write a least-squares solver from scratch in Python/NumPy, using the normal equations first and then a QR decomposition, and compare it with `numpy.linalg.lstsq`.

## Status

**Preparation phase.** The solver itself is not written yet. I am working through a NumPy training programme (`Training/exercices.md`, 80 exercises) that builds every piece the solver needs:

| Section | Topic | Progress |
|---|---|---|
| A | NumPy fundamentals: creation, slicing, masks, vectorisation | done (A1–A10) |
| B | Indexing, broadcasting, statistics | in progress (B11–B15) |
| C | Basic matrix operations | to do |
| D | Least squares: normal equations, residuals, condition number, weighted LS | to do |
| E | QR decomposition and variants | to do |

## Layout

```
Training/A, Training/B    exercise solutions
src/io/csv_io.py          load a CSV into (A, b), last column = b
ressources_and_bibliography.md   papers and notes
```

## Reading

The main reference so far is *Bibliography on total least squares and related methods* (Markovsky, 2010). See `ressources_and_bibliography.md` for notes.
