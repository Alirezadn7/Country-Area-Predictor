# Country Area Prediction

A small Machine Learning project that scrapes country data (population and area) from the web, stores it locally in SQLite, and trains a Decision Tree model to predict a country's area from its population. It is built as a learning exercise for web scraping, data pipelining, and scikit-learn regression.

## Key Features

- **Web scraping** of real country data (population + area) using `requests` and `BeautifulSoup`.
- **Local persistence** with SQLite — no database server required.
- **Supervised regression** model trained with scikit-learn's `DecisionTreeRegressor`.
- **Interactive model testing** — enter a population and get a predicted area.
- **One-command pipeline** that runs scrape → train → test.

## Tech Stack

- Python 3.13
- scikit-learn (Decision Tree Regressor)
- numpy
- requests + BeautifulSoup (web scraping)
- sqlite3 (built-in, local storage)

## Project Structure

```
├── main.py        # Orchestrator: runs scrape → train → test
├── webscrape.py   # Scrapes country data and writes it to SQLite
├── ml.py          # Loads data from SQLite and trains the model
├── predict.py     # Interactive CLI to test the model (with metrics)
├── import sys.py  # Utility class: LCA (Lowest Common Ancestor, binary lifting)
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset Description

The dataset is scraped from `https://www.scrapethissite.com/pages/simple/`. Each of the **250 rows** represents a country with:

| Field        | Type     | Description                          |
|--------------|----------|--------------------------------------|
| `country`    | TEXT     | Country name                         |
| `population` | INTEGER  | Population of the country            |
| `area`       | REAL     | Area in square kilometers (km²)      |

The data is stored locally in `country.db` (a SQLite database), which is generated at runtime and is intentionally **not** committed to the repository.

## ML Pipeline

1. **Scrape** — `webscrape.py` fetches and parses the country list, then inserts records into the `countries` table.
2. **Preprocess** — `ml.py` reads `(population, area)` pairs from SQLite and builds numpy arrays.
3. **Feature** — population is the single input feature; the raw value is used directly (no scaling/normalization).
4. **Train** — a `DecisionTreeRegressor` is fitted to predict `area` from `population`.
5. **Evaluate** — `predict.py` reports regression metrics via cross-validation.

## Installation & Setup

Requires Python 3 and the dependencies in `requirements.txt`.

```bash
# 1. Create a virtual environment (recommended)
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## How to Train the Model

Run the full pipeline (scrape data → train model → interactive test):

```bash
python main.py
```

Or run each step manually:

```bash
python webscrape.py   # 1. Scrape data into country.db
python ml.py          # 2. Train the model
```

## How to Evaluate / Use the Model

Start the interactive tester, which also prints model accuracy:

```bash
python predict.py
```

```
Model score (population -> area):  R² = 0.838   MAE = 83,999
Type a number and press Enter. Enter 'q' to quit.
population -> 1000000
area = 28,051.0
```

Type a population value to see the predicted area. Enter `q`, `quit`, or `exit` to leave.

## Example Usage

```
population -> 84000000
area = 357,021.0
```

## Configuration / Environment Variables

No configuration is required. The SQLite file (`country.db`) is created in the project directory on first run. No credentials or secrets are needed.

## Results / Metrics

Measured inside `predict.py` using 5-fold cross-validation on a Decision Tree model (population → area):

- **R² score:** `0.838` (~84% of variance explained)
- **Mean Absolute Error (MAE):** `83,999 km²`

> Note: metrics are recomputed/reported each time `predict.py` runs.

## Future Improvements

- Store a single clean copy of the data (avoid duplicate rows on repeated scraping).
- Add more predictive features to improve area prediction.
- Add a README-driven reverse model (predict population from area) as a full module.
- Replace hardcoded scraping details with configuration.

## AI Assistance

This project was developed with the assistance of **OpenCode**, used as an AI development assistant for coding, debugging, and refactoring throughout the lifecycle of the project.