# Pandas DataFrame Operations - Day 73

This repository documents my exploration of DataFrame operations in Pandas as part of my #100DaysOfCode challenge.

## Learning Points

- **Grouping Data:**

  - Used `.groupby()` to explore the number of posts and entries per programming language.

- **Datetime Conversion:**

  - Converted strings to Datetime objects with `to_datetime()` for easier plotting.

- **DataFrame Reshaping:**

  - Reshaped DataFrame by converting categories to columns using `.pivot()`.

- **Handling Missing Data:**

  - Used `.count()` and `isna().values.any()` to look for NaN values in our DataFrame.
  - Replaced NaN values using `.fillna()`.

- **Creating Line Charts:**

  - Created multiple line charts using `.plot()` with a for-loop.

- **Chart Styling:**

  - Styled charts by changing the size, labels, and axis bounds.
  - Added a legend to differentiate lines by color.

- **Smoothing Data:**
  - Smoothed out time-series observations with `.rolling().mean()` to better identify trends over time.

## GitHub Repository

Find the code and examples on GitHub:
[GitHub Repository](https://github.com/imnilesh18/Python-Projects)
