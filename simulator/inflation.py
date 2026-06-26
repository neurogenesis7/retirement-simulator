import numpy as np


def apply_inflation(value: float, inflation_rate: float) -> float:
    return value / (1 + inflation_rate)


def stochastic_inflation(mean: float, vol: float, rng: np.random.Generator) -> float:
    return max(0, rng.normal(mean / 12, vol / np.sqrt(12)))