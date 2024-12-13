# Prime Number Game: Maria vs Ben

This repository contains a Python function `isWinner(x, nums)` that determines the winner of a prime number game played between Maria and Ben. They take turns picking prime numbers from a set and removing the selected prime number and its multiples from the set. The player who cannot make a move loses the game.

## Function Overview

The `isWinner` function takes the number of rounds and a list of integers representing the size of the sets in each round. It returns the name of the player who won the most rounds. If the winner cannot be determined, the function returns `None`.

## Input Format

The input to the function consists of:
- `x`: An integer representing the number of rounds.
- `nums`: A list of integers where each integer represents the size of the set (from 1 to n) for each round.

### Example

```python
x = 3
nums = [4, 5, 1]

