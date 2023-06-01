import csv


def clean_action(action):
    name = action["name"]
    price = str(action["price"])
    profit = str(action["profit"])

    # If a data is missing or 0, we can't clean it
    if (
        name == ""
        or name == "name"
        or price == ""
        or price == "price"
        or profit == ""
        or price == "price"
    ):
        return False

    try:
        cleaned_action = {
            "name": name,
            "price": abs(float(price)),
            "profit": abs(float(profit)),
        }
        if cleaned_action["price"] == 0 or cleaned_action["profit"] == 0:
            return False
        return cleaned_action
    except ValueError:
        return False


def read_dataset(dataset_path):
    # read csv file
    actions = {}
    cleaned_actions = {}
    extra_clean_actions = 0
    with open(dataset_path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != "name":
                action = {
                    "name": row[0],
                    "price": row[1],
                    "profit": row[2],
                }
                actions[row[0]] = action
                cleaned_action = clean_action(action)
                if cleaned_action:
                    extra_clean_actions += 1
                    cleaned_actions[row[0]] = cleaned_action

    print(f"\nFinished reading csv file {dataset_path}")
    print(
        f"We were able to use or clean {extra_clean_actions} actions on a total of {len(actions)} actions"
    )

    return cleaned_actions


def merge_datasets(dataset_1, dataset_2):
    merged_dataset = {}
    dataset_1_keys = dataset_1.keys()
    dataset_2_keys = dataset_2.keys()

    for action_name, action in dataset_1.items():
        merged_dataset[action_name] = action

    for action_name, action in dataset_2.items():
        merged_dataset[action_name] = action

    print(f"\nFinished merging datasets")
    print(f"Dataset 1 had {len(dataset_1_keys)} actions")
    print(f"Dataset 2 had {len(dataset_2_keys)} actions")
    print(f"Merged dataset has {len(merged_dataset)} actions")
    print(
        f"Dataset 1 and 2 had {len(set(dataset_1_keys) & set(dataset_2_keys))} actions in common"
    )
    return merged_dataset


dataset_1 = read_dataset("dataset1_Python+P7.csv")
dataset_2 = read_dataset("dataset2_Python+P7.csv")
merged_dataset = merge_datasets(dataset_1, dataset_2)
