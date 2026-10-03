import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    r"")

years = [1800, 1902, 1950, 2000, 2026]

data = df[df["Year"].isin(years)]

x = np.arange(len(years))
width = 0.25

plt.figure(figsize=(12, 6))

plt.bar(
    x - width,
    data["Global_Female_Literacy_Pct"],
    width,
    label="Female Literacy"
)

plt.bar(
    x,
    data["Female_Labor_Force_Pct"],
    width,
    label="Female Labor Force"
)

plt.bar(
    x + width,
    data["Women_In_Parliament_Pct"],
    width,
    label="Women In Parliament"
)

plt.xlabel("Year")
plt.ylabel("Percentage")
plt.title("Feminism Growth History")

plt.xticks(x, years)
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.show()
