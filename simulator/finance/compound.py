"""
Compounding mathematics.

This module contains reusable financial compounding equations.
"""

from __future__ import annotations


def annual_to_monthly_rate(rate: float) -> float:
    """
    Convert an annual effective rate to a monthly effective rate.
    """
    return (1.0 + rate) ** (1.0 / 12.0) - 1.0


def compound_once(balance: float, monthly_return: float) -> float:
    """
    Apply one month of growth.
    """
    return balance * (1.0 + monthly_return)


def compound_series(
    balance: float,
    monthly_returns: list[float],
) -> float:
    """
    Compound through an entire return series.
    """
    for r in monthly_returns:
        balance *= 1.0 + r

    return balance
