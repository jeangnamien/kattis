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
    
    from kattis.oddecho import solve
    
    return mo, sys, Path, project_root, solve


@app.cell
def __(mo):
    mo.md("# Odd Echo")
    return


@app.cell
def __(mo):
    words_input = mo.ui.text_area(value="hello\nworld\nthis\nis\na\ntest", label="Words", rows=6)
    return words_input,


@app.cell
def __(mo, words_input):
    words_input
    return


@app.cell
def __(words_input, solve):
    words = [w.strip() for w in words_input.value.split('\n') if w.strip()]
    result = solve(words)
    return words, result


@app.cell
def __(mo, result):
    mo.md(f"**Output:**\n```\n{chr(10).join(result)}\n```")
    return


if __name__ == "__main__":
    app.run()