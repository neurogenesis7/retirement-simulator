"""
Top-level simulation configuration.

This module exposes SimulationConfig, which combines all
configuration sections into one object used throughout
the retirement simulator.
"""

from dataclasses import dataclass, field

from simulator.config import (
    MarketConfig,
    PortfolioConfig,
    RetirementConfig,
    SimulationOptions,
)


@dataclass(slots=True)
class SimulationConfig:
    """
    Complete configuration for one simulation.
    """

    portfolio: PortfolioConfig = field(default_factory=PortfolioConfig)

    market: MarketConfig = field(default_factory=MarketConfig)

    retirement: RetirementConfig = field(default_factory=RetirementConfig)

    simulation: SimulationOptions = field(default_factory=SimulationOptions)