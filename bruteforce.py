import csv
import time

# check program performance
start_time = time.time()
print("--- Start ---")

# read csv file
size = 3
actions = {}
with open("bruteforce.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != "name" and len(actions) < size:
            actions[row[0]] = {
                "name": row[0],
                "price": row[1],
                "profit": row[2],
            }


print(actions)
budget = 100


def get_investment_price_and_profit(keys):
    return sum([float(actions[key]["price"]) for key in keys]), sum(
        [
            float(actions[key]["profit"]) * float(actions[key]["price"]) * 0.01
            for key in keys
        ]
    )


# print the completed investment with the highest profit

print("--- %s seconds ---" % (time.time() - start_time))
