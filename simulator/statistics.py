import numpy as np


class SimulationStatistics:

    def __init__(self, results: np.ndarray):
        """
        results shape:
        (n_sims, time_steps)
        """
        self.results = results

        # convenience
        self.n_sims, self.time_steps = results.shape

    # ----------------------------
    # BASIC DISTRIBUTIONS
    # ----------------------------

    def quantiles_over_time(self, quantiles=None):
        if quantiles is None:
            quantiles = [0.01, 0.05, 0.10, 0.25, 0.5, 0.75, 0.90, 0.95, 0.99]

        return {q: np.quantile(self.results, q, axis=0) for q in quantiles}

    def final_distribution(self):
        return self.results[:, -1]

    def final_quantiles(self, quantiles=None):
        if quantiles is None:
            quantiles = [0.01, 0.05, 0.10, 0.25, 0.5, 0.75, 0.90, 0.95, 0.99]

        return {q: np.quantile(self.final_distribution(), q) for q in quantiles}

    # ----------------------------
    # RISK METRICS
    # ----------------------------

    def probability_of_ruin(self):
        """
        Ruin = ever hits zero
        """
        ruined = np.any(self.results <= 0, axis=1)
        return np.mean(ruined)

    def survival_probability(self):
        return 1 - self.probability_of_ruin()

    def probability_above_threshold(self, threshold: float):
        final = self.final_distribution()
        return np.mean(final >= threshold)

    # ----------------------------
    # TIME-BASED FAILURE
    # ----------------------------

    def ruin_time_distribution(self):
        """
        Returns when portfolios hit zero.
        If never ruined → time_steps
        """
        ruin_times = []

        for path in self.results:
            hits = np.where(path <= 0)[0]

            if len(hits) == 0:
                ruin_times.append(self.time_steps)
            else:
                ruin_times.append(hits[0])

        return np.array(ruin_times)

    def median_ruin_time(self):
        return np.median(self.ruin_time_distribution())

    # ----------------------------
    # RETIREMENT READINESS METRICS
    # ----------------------------

    def success_rate(self, retirement_start_index: int):
        """
        Success = never hits zero AFTER retirement begins
        """

        post_retirement = self.results[:, retirement_start_index:]

        ruined = np.any(post_retirement <= 0, axis=1)

        return 1 - np.mean(ruined)

    # ----------------------------
    # SUMMARY REPORT
    # ----------------------------

    def summary(self, retirement_start_index: int):
        final = self.final_distribution()

        return {
            "median_final": np.median(final),
            "mean_final": np.mean(final),
            "p5_final": np.quantile(final, 0.05),
            "p95_final": np.quantile(final, 0.95),
            "probability_of_ruin": self.probability_of_ruin(),
            "survival_probability": self.survival_probability(),
            "median_ruin_time": self.median_ruin_time(),
            "retirement_success_rate": self.success_rate(retirement_start_index),
        }
