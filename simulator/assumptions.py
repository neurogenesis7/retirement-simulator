from dataclasses import dataclass


@dataclass
class SimulationConfig:
    # Time
    years: int = 30
    months_per_year: int = 12

    # Portfolio
    initial_portfolio: float = 100_000
    monthly_contribution: float = 1_000
    contribution_growth_rate: float = 0.0  # yearly increase %

    # Market assumptions
    expected_return: float = 0.08
    volatility: float = 0.15

    # Inflation
    inflation_rate: float = 0.03
    inflation_volatility: float = 0.01

    # Simulation control
    n_sims: int = 10_000
    seed: int | None = 42

    # Retirement phase
    withdrawal_rate: float = 0.04