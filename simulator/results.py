"""
Simulation result container.

This dataclass represents the complete output of a simulation run.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from simulator.assumptions import SimulationConfig
from simulator.statistics import SimulationStatistics
from simulator.timeline import Timeline


@dataclass(slots=True)
class SimulationResults:
    """
    Container for one completed simulation.
    """

    config: SimulationConfig

    timeline: Timeline

    paths: np.ndarray

    statistics: SimulationStatistics
