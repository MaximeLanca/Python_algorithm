import csv


def extract_data_from_csv() -> list:
    try:
        with open('./data/Liste+d_actions+-+P7+Python+-+Feuille+1.csv', mode='r', encoding='utf-8') as csvfile:
            actions = list(csv.reader(csvfile))
            del (actions[0])
    except FileNotFoundError:
        print("The file cannot be found.")

    return actions


