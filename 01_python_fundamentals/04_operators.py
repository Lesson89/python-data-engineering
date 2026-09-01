# This is a simple Python program that calculates the profit of a business based on its revenue and cost.

revenue = 250000
cost = 175000

profit = revenue - cost
print("Profit:", profit)

# calculate profit margin
profit_margin = (profit / revenue) * 100
print("Profit Margin:", profit_margin, "%")

#then using f-string to print the profit and profit margin

print(f"profit: {profit}, profit margin: {profit_margin}%")

# Comparison operators

revenue = 250000
cost = 175000
profit = revenue - cost
profit_margin = (profit / revenue) * 100

is_revenue_greater_than_cost = revenue > cost
print("Is revenue greater than cost?", is_revenue_greater_than_cost)

is_profit_grester_than_50000 = profit > 50000
print("Is profit greater than 50000?", is_profit_grester_than_50000)

is_profit_margin_greater_than_30 = profit_margin > 30
print("Is profit margin greater than 30%?", is_profit_margin_greater_than_30)

is_profit_margin_equal_to_30 = profit_margin == 30
print("Is profit margin equal to 30%?", is_profit_margin_equal_to_30)

is_cost_greater_that_or_equal_to_revenue = cost >= revenue
print("Is cost greater than or equal to revenue?", is_cost_greater_that_or_equal_to_revenue)

#=============================================================================================

revenue = 788000
cost = 375000
profit = revenue - cost
profit_margin = (profit / revenue) * 100

#1. Is revenue greater than cost?
is_revenue_greater_than_cost = revenue > cost
print("Is revenue greater than cost?", is_revenue_greater_than_cost) 

# 2. Is profit greater than 50,000?
is_profit_greater_than_50000 = profit > 50000
print("Is profit greater than 50,000?", is_profit_greater_than_50000)

# 3. Is profit margin equal to 30?
is_profit_margin_equal_to_30 = profit_margin == 30
print("Is profit margin equal to 30%?", is_profit_margin_equal_to_30)

# 4. Is cost greater than or equal to revenue?
is_cost_greater_than_or_equal_to_revenue = cost >= revenue
print("Is cost greater than or equal to revenue?", is_cost_greater_than_or_equal_to_revenue)

