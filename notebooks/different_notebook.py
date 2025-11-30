import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sys
    from pathlib import Path

    project_root = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
    sys.path.insert(0, str(project_root / "src"))

    from kattis.acappellarecording import acappella

    return acappella, mo


@app.cell
def _(mo):
    mo.md("""
    # A Cappella Recording
    """)
    return


@app.cell
def _(mo):
    d_input = mo.ui.slider(start=1, stop=100, value=10, label="Max pitch range (d)", show_value=True)
    pitches_input = mo.ui.text_area(value="1\n5\n3\n7\n6", label="Pitches", rows=6)
    return d_input, pitches_input


@app.cell
def _(d_input, mo, pitches_input):
    mo.vstack([d_input, pitches_input])
    return


@app.cell
def _(acappella, d_input, pitches_input):
    try:
        pitches = [int(line.strip()) for line in pitches_input.value.strip().split('\n') if line.strip()]
        result = acappella(len(pitches), d_input.value, pitches.copy())
        error = None
    except Exception as e:
        result = None
        error = str(e)
    return error, result


@app.cell
def _(error, mo, result):
    if error:
        mo.callout(f"Error: {error}", kind="danger")
    elif result:
        mo.md(f"Recording sessions needed: **{result}**")
    return


if __name__ == "__main__":
    app.run()
