from simulator.assumptions import SimulationConfig
from simulator.monte_carlo import MonteCarloEngine
from simulator.statistics import SimulationStatistics

from dashboard.plots import (
    plot_fan_chart,
    plot_final_distribution,
    plot_survival_curve,
)

import plotly.io as pio


config = SimulationConfig(
    years=30,
    retirement_years=30,
    n_sims=2000
)

engine = MonteCarloEngine(config)
results = engine.run()

stats = SimulationStatistics(results)

retirement_start = config.years * 12

quantiles = stats.quantiles_over_time()

# FAN CHART
fig1 = plot_fan_chart(quantiles)
pio.show(fig1)

# HISTOGRAM
fig2 = plot_final_distribution(stats.final_distribution())
pio.show(fig2)

# SURVIVAL
fig3 = plot_survival_curve(results)
pio.show(fig3)

# PRINT SUMMARY
print(stats.summary(retirement_start))