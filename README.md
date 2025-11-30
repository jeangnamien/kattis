# Kattis Solutions

[![Tests and Coverage](https://github.com/jeangnamien/kattis/actions/workflows/tests.yml/badge.svg)](https://github.com/jeangnamien/kattis/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/jeangnamien/ad3e75bc84d929dbe2f7173a79ccf193/raw/kattis-coverage.json)](https://gist.github.com/jeangnamien/ad3e75bc84d929dbe2f7173a79ccf193)
[![Code Quality](https://img.shields.io/badge/pylint-9.97%2F10-brightgreen)](https://github.com/jeangnamien/kattis)

Python solutions to Kattis programming problems with test coverage and automated CI/CD.

## Features

- ✅ **45+ passing tests** with PyTest
- ✅ **9.97/10 PyLint score**
- ✅ **Black** formatted code
- ✅ **CI/CD** with GitHub Actions
- ✅ **Poetry** for dependency management
- ✅ **Interactive Marimo notebooks** for exploration

## Setup
```bash
poetry install
```

## Run tests
```bash
poetry run pytest -v
poetry run coverage run -m pytest
poetry run coverage report -m
```

## Interactive Notebooks

Explore solutions interactively with Marimo:
```bash
poetry run marimo edit notebooks/
```

## Solutions

- `different` - Basic math operations
- `oddecho` - String filtering
- `lvable` - String subsequence matching
- `thirteen_floors` - Floor numbering logic
- `hissingmicrophone` - Pattern detection
- `monopol` - Probability calculation
- `game_2048` - Sliding puzzle game
- `printed_statues` - Optimization problem
- `three_puzzle` - BFS pathfinding
- `acappella` - Greedy scheduling algorithm

## Project Structure
```
kattis/
├── src/kattis/          # Solution implementations
├── tests/               # Unit tests
├── notebooks/           # Interactive Marimo notebooks
├── .github/workflows/   # CI/CD pipeline
└── pyproject.toml       # Poetry configuration
```