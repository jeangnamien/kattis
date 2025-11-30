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
    
    from kattis.thirteen_floors import solve
    
    return mo, sys, Path, project_root, solve


@app.cell
def __(mo):
    mo.md("# Thirteen Floors")
    return


@app.cell
def __(mo):
    floor_slider = mo.ui.slider(start=1, stop=100, value=13, label="American Floor", show_value=True)
    return floor_slider,


@app.cell
def __(mo, floor_slider):
    floor_slider
    return


@app.cell
def __(solve, floor_slider):
    result = solve(floor_slider.value)
    return result,


@app.cell
def __(mo, result, floor_slider):
    mo.md(f"American floor **{floor_slider.value}** → European floor **{result}**")
    return


if __name__ == "__main__":
    app.run()