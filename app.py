from simulator.statistics import SimulationStatistics


def analyze_results(results, retirement_start_index):
    stats = SimulationStatistics(results)

    return {
        "summary": stats.summary(retirement_start_index),
        "quantiles": stats.quantiles_over_time(),
        "final_quantiles": stats.final_quantiles(),
        "ruin_curve": stats.ruin_time_distribution(),
    }