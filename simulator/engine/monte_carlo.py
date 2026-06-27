import numpy as np

from simulator.assumptions import SimulationConfig
from simulator.portfolio import (
    stochastic_return,
    add_contribution,
)
from simulator.withdrawals import (
    initial_annual_withdrawal,
    monthly_withdrawal,
    adjust_for_inflation,
)


class MonteCarloEngine:

    def __init__(self, config: SimulationConfig):
        self.config = config
        self.rng = np.random.default_rng(config.seed)

    def run(self):

        work_months = self.config.years * self.config.months_per_year
        retire_months = self.config.retirement_years * self.config.months_per_year
        total_months = work_months + retire_months

        results = np.zeros((self.config.n_sims, total_months))

        for sim in range(self.config.n_sims):

            portfolio = self.config.initial_portfolio

            # initial withdrawal setup
            annual_withdrawal = initial_annual_withdrawal(
                portfolio,
                self.config.withdrawal_rate
            )
            monthly_withdraw = monthly_withdrawal(annual_withdrawal)

            inflation_multiplier = 1.0

            for t in range(total_months):

                # stochastic return
                r = stochastic_return(
                    self.config.expected_return,
                    self.config.volatility,
                    self.rng
                )

                # -------------------------
                # ACCUMULATION PHASE
                # -------------------------
                if t < work_months:

                    portfolio = add_contribution(
                        portfolio,
                        self.config.monthly_contribution
                    )

                # -------------------------
                # RETIREMENT PHASE
                # -------------------------
                else:

                    # inflation adjustment (optional)
                    if self.config.withdrawal_adjust_for_inflation:
                        infl = self.rng.normal(
                            self.config.inflation_rate / 12,
                            self.config.inflation_volatility / np.sqrt(12)
                        )
                        inflation_multiplier *= (1 + infl)

                        current_withdraw = monthly_withdraw * inflation_multiplier
                    else:
                        current_withdraw = monthly_withdraw

                    portfolio -= current_withdraw

                    # prevent negative spiral
                    portfolio = max(portfolio, 0)

                # grow portfolio
                portfolio *= (1 + r)

                results[sim, t] = portfolio

                # stop if ruined (optional efficiency shortcut)
                if portfolio <= 0:
                    results[sim, t:] = 0
                    break

        return results