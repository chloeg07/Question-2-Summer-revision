#Question 2
Hours = [12, 7, 9, 9, 6, 8, 2]
total_litres = sum(Hours) * 0.5
cost_per_litre = 1.35
total_cost = total_litres * cost_per_litre
total_cost_rounded = round(total_cost, 1)
print("Total cost of milk during the week: €{}" .format(total_cost_rounded))

