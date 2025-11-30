import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import sys
    from pathlib import Path
    
    project_root = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
    sys.path.insert(0, str(project_root / "src"))
    
    from kattis.game_2048 import move_left, move_right, move_up, move_down
    
    return mo, plt, sns, np, sys, Path, project_root, move_left, move_right, move_up, move_down


@app.cell
def __(mo):
    mo.md("# 2048 Game Simulator")
    return


@app.cell
def __(mo):
    board_text = mo.ui.text_area(value="2 0 0 2\n0 2 0 0\n0 0 2 0\n0 0 0 2", label="Board", rows=5)
    direction = mo.ui.dropdown(options=["left", "right", "up", "down"], value="left", label="Direction")
    return board_text, direction


@app.cell
def __(mo, board_text, direction):
    mo.vstack([board_text, direction])
    return


@app.cell
def __(board_text, direction, move_left, move_right, move_up, move_down):
    try:
        board = [[int(x) for x in line.split()] for line in board_text.value.strip().split('\n')]
        if direction.value == "left":
            new_board = move_left(board)
        elif direction.value == "right":
            new_board = move_right(board)
        elif direction.value == "up":
            new_board = move_up(board)
        else:
            new_board = move_down(board)
        error = None
    except Exception as e:
        new_board = None
        error = str(e)
    return board, new_board, error


@app.cell
def __(mo, new_board, error):
    if error:
        mo.callout(f"Error: {error}", kind="danger")
    elif new_board:
        mo.md(f"```\n{chr(10).join(' '.join(str(c).rjust(4) for c in r) for r in new_board)}\n```")
    return


@app.cell
def __(plt, sns, np, board, new_board, error):
    if not error and new_board:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        sns.heatmap([[np.log2(x+1) for x in r] for r in board], annot=board, fmt='d', cmap='YlOrRd', ax=ax1, cbar=False, square=True)
        sns.heatmap([[np.log2(x+1) for x in r] for r in new_board], annot=new_board, fmt='d', cmap='YlOrRd', ax=ax2, cbar=False, square=True)
        ax1.set_title('Before')
        ax2.set_title('After')
        ax1.axis('off')
        ax2.axis('off')
        plt.gca()
    return fig, ax1, ax2


if __name__ == "__main__":
    app.run()