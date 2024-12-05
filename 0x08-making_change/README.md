# Make Change Function

This repository contains a Python function `makeChange(coins, total)` that determines the fewest number of coins needed to meet a given total amount.

## Function Overview

The `makeChange` function takes a list of coin values and a total amount, and returns the fewest number of coins needed to make that amount. If the total amount is 0 or less, the function returns 0. If the total cannot be met by any combination of coins, the function returns -1.

## Input Format

The input to the function consists of:
- `coins`: A list of integers representing the values of the coins you have. Each coin value is greater than 0.
- `total`: An integer representing the total amount you want to achieve.

### Example

```python
coins = [1, 2, 5]
total = 11

