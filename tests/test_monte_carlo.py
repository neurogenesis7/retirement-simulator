"""
Tests for Monte Carlo engine.
"""

from simulator.assumptions import SimulationConfig
from simulator.config import (
    PortfolioConfig,
    RetirementConfig,
    SimulationOptions,
)

from simulator.monte_carlo import MonteCarloEngine


def test_output_shape():
    """
    Monte Carlo engine should return
    (simulations, total_months)
    """

    cfg = SimulationConfig(
        portfolio=PortfolioConfig(
            initial_value=100_000,
            monthly_contribution=1000,
        ),
        retirement=RetirementConfig(
            accumulation_years=10,
            retirement_years=20,
        ),
        simulation=SimulationOptions(
            simulations=100,
        ),
    )

    engine = MonteCarloEngine(cfg)

    paths = engine.run()

    assert paths.shape == (100, 360)


def test_all_paths_non_negative():
    """
    Portfolio values should never become negative.
    """

    cfg = SimulationConfig(
        simulation=SimulationOptions(
            simulations=50,
        )
    )

    engine = MonteCarloEngine(cfg)

    paths = engine.run()

    assert (paths >= 0).all()