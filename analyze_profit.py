def analyze_profit(gains,expenses):
    profit = gains - expenses
    after_taxes = 0.90 * profit
    above_mean = profit > 1000
    return profit, after_taxes, above_mean

insights = analyze_profit(3000,1200)
print(f"profit: {insights[0]}")
print(f"above_mean: {insights[2]}")