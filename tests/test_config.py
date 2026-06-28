"""
Tests for simulation configuration validation.
"""

import pytest

from simulator.assumptions import SimulationConfig
from simulator.config import (
    MarketConfig,
    PortfolioConfig,
    RetirementConfig,
    SimulationOptions,
)


def test_default_config_constructs():
    """Default configuration should construct successfully."""
    cfg = SimulationConfig()

    assert cfg.portfolio.initial_value == 100_000.0
    assert cfg.market.expected_return == 0.08
    assert cfg.retirement.accumulation_years == 30
    assert cfg.simulation.simulations == 10_000


def test_negative_volatility():
    """Negative volatility should raise an error."""
    with pytest.raises(ValueError):
        MarketConfig(volatility=-0.10)


def test_invalid_accumulation_years():
    """Accumulation years must be positive."""
    with pytest.raises(ValueError):
        RetirementConfig(accumulation_years=0)


def test_invalid_simulation_count():
    """Simulation count must be positive."""
    with pytest.raises(ValueError):
        SimulationOptions(simulations=0)


def test_negative_initial_portfolio():
    """Portfolio value cannot be negative."""
    with pytest.raises(ValueError):
        PortfolioConfig(initial_value=-100)
