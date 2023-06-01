import csv
import time
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


def run_optimized(actions, size=20, budget=500):
    # check program performance
    start_time = time.time()
    print("--- Start ---")
    actions = {key: value for key, value in list(actions.items())[:size]}
    actions_by_calculated_profit = sorted(
        actions.items(),
        key=lambda x: float(x[1]["profit"]) * float(x[1]["price"]),
        reverse=True,
    )

    total_price = 0
    investment = {"actions": [], "total_price": 0, "total_profit": 0}
    while total_price <= budget and len(actions_by_calculated_profit) > 0:
        best_profit_action = actions_by_calculated_profit.pop()
        if total_price + float(best_profit_action[1]["price"]) > budget:
            # this pops out actions that are too expensive for the current budget
            continue
        total_price += float(best_profit_action[1]["price"])
        investment["actions"].append(best_profit_action[0])
        investment["total_price"] += float(best_profit_action[1]["price"])
        investment["total_profit"] += (
            float(best_profit_action[1]["profit"])
            * float(best_profit_action[1]["price"])
            * 0.01
        )

    # print the completed investment with the highest profit
    print(investment)
    print("--- End %s seconds ---" % (time.time() - start_time))
    print("")

    return investment, (time.time() - start_time)


def graph_optimized():
    execution_times = []
    for x in range(20):
        # We are running the optimized algorithm 10 times for each number of actions
        current_execution_times = []
        for _ in range(10):
            _, execution_time = run_optimized(actions, size=x + 1)
            current_execution_times.append(execution_time)
        execution_times.append(
            sum(current_execution_times) / len(current_execution_times)
        )

    # plotting the points
    plt.plot(range(1, len(execution_times) + 1), execution_times)

    # naming
    plt.xlabel("Number of actions")
    plt.ylabel("Processing time (seconds)")
    plt.title("optimized time to best possible investment with 500 budget")

    # show the plot
    plt.show()


graph_optimized()
