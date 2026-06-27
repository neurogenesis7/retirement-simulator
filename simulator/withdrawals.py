def initial_annual_withdrawal(portfolio: float, rate: float) -> float:
    return portfolio * rate


def monthly_withdrawal(annual_withdrawal: float) -> float:
    return annual_withdrawal / 12


def adjust_for_inflation(amount: float, inflation_rate: float) -> float:
    return amount * (1 + inflation_rate)