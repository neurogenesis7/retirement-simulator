from dataclasses import dataclass

import numpy as np

from simulator.assumptions import SimulationConfig
from simulator.statistics import SimulationStatistics


@dataclass
class SimulationResults:
    paths: np.ndarray
    statistics: SimulationStatistics
    summary: dict
    quantiles: dict
    final_distribution: np.ndarray
    final_quantiles: dict