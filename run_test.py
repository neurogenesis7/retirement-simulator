"""
Development test harness.

Run this script to verify the simulator,
statistics layer, and plotting layer all
work together.
"""

from simulator.assumptions import SimulationConfig
from simulator.controller import SimulationController

from dashboard.plots import (
    plot_fan_chart,
    plot_final_distribution,
    plot_survival_curve,
)

import plotly.io as pio


def main():

    config = SimulationConfig()

    controller = SimulationController(config)

    simulation = controller.run()

    stats = simulation.statistics

    summary = stats.summary(simulation.timeline.retirement_month)

    print("\n===== SUMMARY =====")

    for key, value in summary.items():
        print(f"{key:30s}: {value}")

    fan_chart = plot_fan_chart(stats.quantiles_over_time())

    histogram = plot_final_distribution(stats.final_distribution())

    survival = plot_survival_curve(simulation.paths)

    pio.show(fan_chart)
    pio.show(histogram)
    pio.show(survival)


if __name__ == "__main__":
    main()
