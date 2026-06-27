from dataclasses import dataclass

import numpy as np


@dataclass
class Timeline:

    work_years: int
    retirement_years: int

    @property
    def total_months(self):
        return (self.work_years + self.retirement_years) * 12

    @property
    def month_index(self):
        return np.arange(self.total_months)

    @property
    def year_index(self):
        return self.month_index / 12

    @property
    def retirement_month(self):
        return self.work_years * 12

    @property
    def retirement_year(self):
        return self.work_years