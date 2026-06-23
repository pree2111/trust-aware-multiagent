import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import pandas as pd

from coalition.shapley import (
    Shapley
)

df = pd.read_csv(
    "results/results.csv"
)

calculator = (
    Shapley()
)

values = calculator.calculate(
    df
)

print()

print(
    "===== SHAPLEY VALUES ====="
)

print()

for agent, value in sorted(
    values.items(),
    key=lambda x: x[1],
    reverse=True
):

    print(
        f"{agent}: {value:.4f}"
    )
