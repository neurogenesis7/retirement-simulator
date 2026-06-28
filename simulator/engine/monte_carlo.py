"""
Monte Carlo simulation engine.

This module simulates portfolio accumulation and retirement
withdrawals using a configurable return generator.
"""

from __future__ import annotations

import numpy as np

from simulator.assumptions import SimulationConfig
from simulator.return_models.normal import NormalReturnGenerator
from simulator.timeline import Timeline
from simulator.withdrawals import (
    adjust_for_inflation,
    initial_annual_withdrawal,
    monthly_withdrawal,
)


class MonteCarloEngine:
    """
    Runs Monte Carlo retirement simulations.
    """

    def __init__(self, config: SimulationConfig):
        self.config = config

        self.rng = np.random.default_rng(config.simulation.random_seed)

        self.timeline = Timeline(
            work_years=config.retirement.accumulation_years,
            retirement_years=config.retirement.retirement_years,
        )

        self.return_generator = NormalReturnGenerator(
            mean=config.market.expected_return,
            volatility=config.market.volatility,
            rng=self.rng,
        )

    def run(self) -> np.ndarray:
        """
        Execute the Monte Carlo simulation.

        Returns
        -------
        np.ndarray
            Shape:
            (simulations, total_months)
        """

        n_sims = self.config.simulation.simulations
        total_months = self.timeline.total_months

        results = np.zeros((n_sims, total_months))

        for sim in range(n_sims):

            portfolio = self.config.portfolio.initial_value

            annual_withdrawal = initial_annual_withdrawal(
                portfolio,
                self.config.retirement.withdrawal_rate,
            )

            monthly_withdraw = monthly_withdrawal(annual_withdrawal)

            inflation_multiplier = 1.0

            for month in range(total_months):

                monthly_return = self.return_generator.next_return()

                # ----------------------------
                # Accumulation phase
                # ----------------------------
                if month < self.timeline.retirement_month:

                    portfolio += self.config.portfolio.monthly_contribution

                # ----------------------------
                # Retirement phase
                # ----------------------------
                else:

                    if self.config.retirement.inflation_adjusted_withdrawals:

                        inflation = self.rng.normal(
                            self.config.market.inflation_rate / 12,
                            self.config.market.inflation_volatility / np.sqrt(12),
                        )

                        inflation_multiplier *= 1 + inflation

                        withdrawal = adjust_for_inflation(
                            monthly_withdraw,
                            inflation_multiplier - 1,
                        )

                    else:

                        withdrawal = monthly_withdraw

                    portfolio -= withdrawal

                    portfolio = max(portfolio, 0)

                portfolio *= 1 + monthly_return

                results[sim, month] = portfolio

                if portfolio <= 0:

                    results[sim, month:] = 0

                    break

        return results
