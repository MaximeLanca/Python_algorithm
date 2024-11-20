from extract_csv_data import extract_data_from_csv


def calculates_investisment_group():
    actions_selected = []
    sublist = []
    investment_list = []
    actions_catalog = extract_data_from_csv()
    combination_of_actions = scans_actions_catalog(actions_catalog)

    for actions in combination_of_actions:
        profits = int()
        wallet_customers = 0
        for action in actions:
            wallet_customers += int(action[1])
            if wallet_customers > 500:
                wallet_customers -= int(action[1])
                break
            elif wallet_customers == 500:
                break
            action_profit = action[2].replace("%", "")
            profits += int(action_profit)
        investment_list.append([combination_of_actions.index(actions), profits])

    investment_sorted = sorted(investment_list, key=lambda x: x[1], reverse=True)
    print(f"The best investment is: Investment n° {investment_sorted[0][0]} with a profit of {investment_sorted[0][1]} %")




def scans_actions_catalog(actions_catalog_list) -> list:
    combination_of_actions = []
    for i in range(len(actions_catalog_list)):
        actions_catalog_recomposed = actions_catalog_list[-i:] + actions_catalog_list[:-i]
        actions_selected = []
        for action in actions_catalog_recomposed:
            if action not in actions_selected:
                actions_selected.append(action)
        combination_of_actions.append(actions_selected)
    return combination_of_actions
    # print(combination_of_actions[1])
    # print(combination_of_actions[0])
    # print(combination_of_actions[2])
