import numpy as np

from simulator.portfolio import yearly_to_monthly
from simulator.return_models.base import ReturnGenerator


class NormalReturnGenerator(ReturnGenerator):

    def __init__(self, mean, volatility, rng):
        self.monthly_mean = yearly_to_monthly(mean)
        self.monthly_vol = volatility / np.sqrt(12)
        self.rng = rng

    def next_return(self):
        return self.rng.normal(self.monthly_mean, self.monthly_vol)
