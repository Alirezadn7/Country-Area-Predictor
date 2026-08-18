import sqlite3
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error
import numpy as np


def load_data():
    conn = sqlite3.connect('country.db')
    rows = conn.execute("SELECT population, area FROM countries").fetchall()
    conn.close()
    return rows


def evaluate(model, x, y):
    r2 = cross_val_score(model, x, y, cv=5).mean()
    mae = mean_absolute_error(y, model.fit(x, y).predict(x))
    return r2, mae


def main():
    data = load_data()
    if not data:
        print("No data found. Run: python webscrape.py")
        return

    x = np.array([[p, a] for p, a in data])
    pop = x[:, 0].reshape(-1, 1)
    area = x[:, 1]

    model = tree.DecisionTreeRegressor()
    r2, mae = evaluate(model, pop, area)
    print(f"Model score (population -> area):  R² = {r2:.3f}   MAE = {mae:,.0f}")

    pop2area = model
    area2pop = tree.DecisionTreeRegressor().fit(x[:, 1].reshape(-1, 1), x[:, 0])

    print("Type a number and press Enter. Enter 'q' to quit.")
    while True:
        try:
            raw = input("population -> ")
            if raw.lower() in ('q', 'quit', 'exit'):
                break
            p = float(raw)
            print(f"area = {pop2area.predict([[p]])[0]:,.1f}")
        except ValueError:
            print("Not a number.")


if __name__ == "__main__":
    main()