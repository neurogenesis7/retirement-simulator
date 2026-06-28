import numpy as np


def apply_return(value: float, monthly_return: float) -> float:
    return value * (1 + monthly_return)


def add_contribution(value: float, contribution: float) -> float:
    return value + contribution


def yearly_to_monthly(rate: float) -> float:
    return (1 + rate) ** (1 / 12) - 1


def stochastic_return(
    mean_annual: float, vol_annual: float, rng: np.random.Generator
) -> float:
    """
    Lognormal-style approximation using normal shocks.
    """
    monthly_mean = yearly_to_monthly(mean_annual)
    monthly_vol = vol_annual / np.sqrt(12)

    return rng.normal(monthly_mean, monthly_vol)
