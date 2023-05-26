import csv
import time
from itertools import combinations

# read csv file
actions = {}
with open("bruteforce.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != "name":
            actions[row[0]] = {
                "name": row[0],
                "price": row[1],
                "profit": row[2],
            }


def get_investment_price_and_profit(keys):
    return sum([float(actions[key]["price"]) for key in keys]), sum(
        [
            float(actions[key]["profit"]) * float(actions[key]["price"]) * 0.01
            for key in keys
        ]
    )


def all_combinations(items_list):
    result = []
    for i in range(1, len(items_list) + 1):
        for combo in combinations(items_list, i):
            result.append(combo)
    return result


# check program performance
start_time = time.time()
print("--- Start ---")

size = 20
actions = {key: value for key, value in list(actions.items())[:size]}

budget = 500

result = all_combinations(actions.keys())

investments = []
for combo in result:
    price, profit = get_investment_price_and_profit(list(combo))
    investments.append(
        {"actions": list(combo), "total_price": price, "total_profit": profit}
    )

investments = [
    investment for investment in investments if investment["total_price"] <= budget
]
investments = sorted(investments, key=lambda x: x["total_profit"], reverse=True)

print(investments[0])

# print the completed investment with the highest profit

print("--- %s seconds ---" % (time.time() - start_time))
