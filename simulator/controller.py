"""
Simulation controller.

Coordinates the simulation engine and statistical analysis.
"""

from __future__ import annotations

from simulator.assumptions import SimulationConfig
from simulator.monte_carlo import MonteCarloEngine
from simulator.results import SimulationResults
from simulator.statistics import SimulationStatistics


class SimulationController:
    """
    High-level entry point for running simulations.
    """

    def __init__(self, config: SimulationConfig):
        self.config = config

    def run(self) -> SimulationResults:
        """
        Execute one complete retirement simulation.
        """

        engine = MonteCarloEngine(self.config)

        paths = engine.run()

        statistics = SimulationStatistics(paths)

        return SimulationResults(
            config=self.config,
            timeline=engine.timeline,
            paths=paths,
            statistics=statistics,
        )
