from simulator.assumptions import SimulationConfig
from simulator.monte_carlo import MonteCarloEngine


def test_output_shape():

    cfg = SimulationConfig(
        years=10,
        retirement_years=20,
        n_sims=100
    )

    engine = MonteCarloEngine(cfg)

    paths = engine.run()

    assert paths.shape == (100, 360)