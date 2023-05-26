import csv
import time

# check program performance
start_time = time.time()

# read csv file
actions = []
with open("bruteforce.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        actions.append(
            {
                "name": row[0],
                "price": row[1],
                "profit": row[2],
            }
        )

# remove header
actions.pop(0)

total_price = 0
budget = 500
investments = []
completed_investments = []


def add_action_to_investiment(investment, action):
    new_investment = {**investment}
    price = float(action["price"])
    profit = float(action["profit"])
    if action["name"] not in new_investment["actions"]:
        new_investment["actions"].append(action["name"])
        new_investment["total_price"] += price
        new_investment["total_profit"] += profit * price * 0.01
    if new_investment["total_price"] <= budget:
        return new_investment
    else:
        return False


# print the completed investment with the highest profit
print(max(completed_investments, key=lambda x: x["total_profit"]))

print("--- %s seconds ---" % (time.time() - start_time))
