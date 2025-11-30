import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import sys
    from pathlib import Path
    
    project_root = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
    sys.path.insert(0, str(project_root / "src"))
    
    from kattis.three_puzzle import solve
    
    return mo, sys, Path, project_root, solve


@app.cell
def __(mo):
    mo.md("# Three Puzzle")
    return


@app.cell
def __(mo):
    puzzle_input = mo.ui.text_area(value="1 2 3\n4 5 6\n7 8 0", label="Puzzle (3x3)", rows=4)
    return puzzle_input,


@app.cell
def __(mo, puzzle_input):
    puzzle_input
    return


@app.cell
def __(puzzle_input, solve):
    try:
        puzzle = [[int(x) for x in line.split()] for line in puzzle_input.value.strip().split('\n')]
        result = solve(puzzle)
        error = None
    except Exception as e:
        result = None
        error = str(e)
    return puzzle, result, error


@app.cell
def __(mo, result, error):
    if error:
        mo.callout(f"Error: {error}", kind="danger")
    elif result is not None:
        mo.md(f"Minimum moves: **{result}**")
    return


if __name__ == "__main__":
    app.run()