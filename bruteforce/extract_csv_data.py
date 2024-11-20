import csv


def extract_data_from_csv() -> list:
    try:
        with open('./data/Liste+d_actions+-+P7+Python+-+Feuille+1.csv', mode='r', encoding='utf-8') as csvfile:
            lines = csv.reader(csvfile)
            data_csv_file = [line for line in lines]
            del(data_csv_file[0])
    except FileNotFoundError:
        print("The file cannot be found.")

    return data_csv_file


