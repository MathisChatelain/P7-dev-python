import csv
import time
from itertools import combinations
import matplotlib.pyplot as plt

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


def get_investment_price_and_profit(keys, actions):
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


def run_bruteforce(actions, size=20, budget=500):
    # check program performance
    start_time = time.time()
    print("--- Start ---")
    actions = {key: value for key, value in list(actions.items())[:size]}

    result = all_combinations(actions.keys())

    investments = []
    for combo in result:
        price, profit = get_investment_price_and_profit(list(combo), actions)
        investments.append(
            {"actions": list(combo), "total_price": price, "total_profit": profit}
        )

    investments = [
        investment for investment in investments if investment["total_price"] <= budget
    ]
    investments = sorted(investments, key=lambda x: x["total_profit"], reverse=True)

    # print the completed investment with the highest profit
    print(investments[0])
    print("--- End %s seconds ---" % (time.time() - start_time))
    print("")

    return investments[0], (time.time() - start_time)


def graph_bruteforce():
    execution_times = []
    for x in range(10):
        # We are running the bruteforce algorithm 10 times for each number of actions
        current_execution_times = []
        for _ in range(10):
            _, execution_time = run_bruteforce(actions, size=x + 1)
            current_execution_times.append(execution_time)
        execution_times.append(
            sum(current_execution_times) / len(current_execution_times)
        )

    # plotting the points
    plt.plot(range(1, len(execution_times) + 1), execution_times)

    # naming
    plt.xlabel("Number of actions")
    plt.ylabel("Processing time (seconds)")
    plt.title("Bruteforce time to best possible investment with 500 budget")

    # show the plot
    plt.show()


# graph_bruteforce()
print(
    get_investment_price_and_profit(
        [
            "Action-14",
            "Action-17",
            "Action-15",
            "Action-16",
            "Action-1",
            "Action-18",
            "Action-7",
            "Action-8",
            "Action-2",
            "Action-19",
            "Action-9",
            "Action-11",
            "Action-3",
            "Action-13",
            "Action-10",
            "Action-12",
        ],
        actions,
    )
)
