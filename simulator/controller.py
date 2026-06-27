from simulator.monte_carlo import MonteCarloEngine
from simulator.statistics import SimulationStatistics
from simulator.results import SimulationResults


class SimulationController:

    def __init__(self, config):
        self.config = config

    def run(self):

        engine = MonteCarloEngine(self.config)

        paths = engine.run()

        stats = SimulationStatistics(paths)

        retirement_start = (
            self.config.years *
            self.config.months_per_year
        )

        return SimulationResults(
            paths=paths,
            statistics=stats,
            summary=stats.summary(retirement_start),
            quantiles=stats.quantiles_over_time(),
            final_distribution=stats.final_distribution(),
            final_quantiles=stats.final_quantiles(),
        )