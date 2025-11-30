import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import sys
    from pathlib import Path
    
    project_root = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
    sys.path.insert(0, str(project_root / "src"))
    
    from kattis.monopol import calculate_probability
    
    return mo, plt, sys, Path, project_root, calculate_probability


@app.cell
def __(mo):
    mo.md("# Monopoly Probability")
    return


@app.cell
def __(mo):
    positions_input = mo.ui.text(value="3,5,7,9,11", label="Hotel positions (comma-separated)")
    return positions_input,


@app.cell
def __(mo, positions_input):
    positions_input
    return


@app.cell
def __(positions_input, calculate_probability):
    try:
        positions = [int(x.strip()) for x in positions_input.value.split(',')]
        prob = calculate_probability(len(positions), positions)
        error = None
    except Exception as e:
        prob = None
        error = str(e)
        positions = []
    return positions, prob, error


@app.cell
def __(mo, prob, error):
    if error:
        mo.callout(f"Error: {error}", kind="danger")
    elif prob:
        mo.md(f"Probability: **{prob:.6f}** ({prob*100:.2f}%)")
    return


@app.cell
def __(plt, prob, error):
    if not error and prob:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(['Hit', 'Miss'], [prob, 1-prob], color=['red', 'green'])
        ax.set_ylabel('Probability')
        ax.set_title('Hotel Landing Probability')
        plt.gca()
    return fig, ax


if __name__ == "__main__":
    app.run()