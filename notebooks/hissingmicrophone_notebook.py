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
    
    from kattis.hissingmicrophone import solve
    
    return mo, sys, Path, project_root, solve


@app.cell
def __(mo):
    mo.md("# Hissing Microphone")
    return


@app.cell
def __(mo):
    text_input = mo.ui.text(value="hiss", label="Text to check")
    return text_input,


@app.cell
def __(mo, text_input):
    text_input
    return


@app.cell
def __(solve, text_input):
    result = solve(text_input.value)
    return result,


@app.cell
def __(mo, result, text_input):
    icon = "🐍" if result == "hiss" else "✅"
    mo.md(f"{icon} **{text_input.value}**: {result}")
    return icon,


if __name__ == "__main__":
    app.run()