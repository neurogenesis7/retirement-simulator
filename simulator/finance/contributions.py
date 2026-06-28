"""
Contribution calculations.
"""

from __future__ import annotations


def contribution_for_month(
    base_contribution: float,
    annual_growth: float,
    month: int,
) -> float:
    """
    Calculate the contribution for a given month.
    """

    years = month / 12.0

    return base_contribution * ((1 + annual_growth) ** years)
