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
    
    from kattis.printed_statues import solve
    
    return mo, sys, Path, project_root, solve


@app.cell
def __(mo):
    mo.md("# Printed Statues")
    return


@app.cell
def __(mo):
    n_slider = mo.ui.slider(start=1, stop=1000, value=10, label="Number of statues", show_value=True)
    return n_slider,


@app.cell
def __(mo, n_slider):
    n_slider
    return


@app.cell
def __(solve, n_slider):
    result = solve(n_slider.value)
    return result,


@app.cell
def __(mo, result, n_slider):
    mo.md(f"To make **{n_slider.value}** statues: **{result}** days")
    return


if __name__ == "__main__":
    app.run()