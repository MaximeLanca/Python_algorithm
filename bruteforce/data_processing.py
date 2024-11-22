from extract_csv_data import extract_data_from_csv
from itertools import combinations

actions_test = extract_data_from_csv()
BUDGET = 500
actions = [
    ("Action-1", 20, 5), ("Action-2", 30, 10), ("Action-3", 50, 15),
    ("Action-4", 70, 20), ("Action-5", 60, 17), ("Action-6", 80, 25),
    ("Action-7", 22, 7), ("Action-8", 26, 11), ("Action-9", 48, 13),
    ("Action-10", 34, 27), ("Action-11", 42, 17), ("Action-12", 110, 9),
    ("Action-13", 38, 23), ("Action-14", 14, 1), ("Action-15", 18, 3),
    ("Action-16", 8, 8), ("Action-17", 4, 12), ("Action-18", 10, 14),
    ("Action-19", 24, 21), ("Action-20", 114, 18)
]


def calculate_profit(action):
    cost, percentage = action[1], action[2]
    return cost * (percentage / 100)


def find_best_investment(actions, budget):
    best_profit = 0
    best_combination = []

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = sum(action[1] for action in combination)
            if total_cost <= budget:
                total_profit = sum(calculate_profit(action) for action in combination)
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = combination

    return best_combination, best_profit


def show_the_results():
    best_combination, best_profit = find_best_investment(actions, BUDGET)
    print("Best combination of actions :")
    for action in best_combination:
        print(f"- {action[0]} (Values: {action[1]} €, Profits: {action[2]}%)")
    print(f"Total values: {best_profit:.2f} €")

# from extract_csv_data import extract_data_from_csv
#
#
# def calculates_investisment_group():
#    investment_list = []
#    actions_catalog = extract_data_from_csv()
#    combination_of_actions = scans_actions_catalog(actions_catalog)
#
#    for actions in combination_of_actions:
#        profits = int()
#        wallet_customers = 0
#        for action in actions:
#            wallet_customers += int(action[1])
#            if wallet_customers > 500:
#                wallet_customers -= int(action[1])
#                break
#            elif wallet_customers == 500:
#                break
#            action_profit = action[2].replace("%", "")
#            profits += int(action_profit)
#        investment_list.append([combination_of_actions.index(actions), profits])
#
#    investment_sorted = sorted(investment_list, key=lambda x: x[1], reverse=True)
#    print(f"The best investment is: Investment n° {investment_sorted[0][0]} with a profit of {investment_sorted[0][1]} %")
#
#
# def scans_actions_catalog(actions_catalog_list) -> list:
#    combination_of_actions = []
#    for i in range(len(actions_catalog_list)):
#        actions_catalog_recomposed = actions_catalog_list[-i:] + actions_catalog_list[:-i]
#        actions_selected = []
#        for action in actions_catalog_recomposed:
#            if action not in actions_selected:
#                actions_selected.append(action)
#        combination_of_actions.append(actions_selected)
#    return combination_of_actions
#
