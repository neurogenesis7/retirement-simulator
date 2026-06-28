"""
Configuration models for the Retirement Simulator.

These dataclasses organize simulation parameters into logical groups.
The top-level SimulationConfig aggregates all configuration sections
used throughout the application.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PortfolioConfig:
    """
    Portfolio accumulation settings.
    """

    initial_value: float = 100_000.0
    monthly_contribution: float = 1_000.0
    annual_contribution_growth: float = 0.00

    def __post_init__(self):
        if self.initial_value < 0:
            raise ValueError("Initial portfolio value cannot be negative.")

        if self.monthly_contribution < 0:
            raise ValueError("Monthly contribution cannot be negative.")


@dataclass(slots=True)
class MarketConfig:
    """
    Market assumptions.
    """

    expected_return: float = 0.08
    volatility: float = 0.15

    inflation_rate: float = 0.03
    inflation_volatility: float = 0.01

    def __post_init__(self):
        if self.expected_return <= -1:
            raise ValueError("Expected return must be greater than -100%.")

        if self.volatility < 0:
            raise ValueError("Volatility must be non-negative.")

        if self.inflation_rate < 0:
            raise ValueError("Inflation cannot be negative.")

        if self.inflation_volatility < 0:
            raise ValueError("Inflation volatility cannot be negative.")


@dataclass(slots=True)
class RetirementConfig:
    """
    Retirement assumptions.
    """

    accumulation_years: int = 30
    retirement_years: int = 30

    withdrawal_rate: float = 0.04
    inflation_adjusted_withdrawals: bool = True

    def __post_init__(self):
        if self.accumulation_years <= 0:
            raise ValueError("Accumulation years must be positive.")

        if self.retirement_years <= 0:
            raise ValueError("Retirement years must be positive.")

        if not (0 <= self.withdrawal_rate <= 1):
            raise ValueError("Withdrawal rate must be between 0 and 1.")


@dataclass(slots=True)
class SimulationOptions:
    """
    Monte Carlo simulation settings.
    """

    simulations: int = 10_000
    random_seed: int | None = 42
    months_per_year: int = 12

    def __post_init__(self):
        if self.simulations <= 0:
            raise ValueError("Simulation count must be positive.")

        if self.months_per_year != 12:
            raise ValueError("Months per year must equal 12.")
