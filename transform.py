import csv
import os
import pandas as pd


#---------------------Abi funktsioonid---------------------
def get_data(arr, file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            arr.append(row)

    del arr[1]
    return arr


def is_number(item):
    try:
        float(item)
        return True
    except ValueError:
        return False

#---------------------Puhastamise funktsioonid---------------------
def clean_data(data):
        r = 0
        for row in data:
            c = 0
            for item in row:
                if item == "..":
                    data[r][c] = None
                else:
                    try:
                        data[r][c] = float(item)
                    except (ValueError, TypeError):
                        pass
                c += 1
            r += 1


def fill_by_100_rule(data, df, group_cols, value_col, pair_values):
    """
    group_cols – veerud, mille alusel andmed grupeeritakse
    value_col – veerg, millest otsitakse vastav paar
    pair_values – kaks väärtust, mille summa peab olema 100
    """

    for keys, group in df.groupby(group_cols):

        values = set(group[value_col])
        if values != set(pair_values):
            continue

        idx1 = group[group[value_col] == pair_values[0]].index[0]
        idx2 = group[group[value_col] == pair_values[1]].index[0]

        r1 = idx1 + 2
        r2 = idx2 + 2

        row1 = data[r1]
        row2 = data[r2]

        for c in range(4, 12):
            a = row1[c]
            b = row2[c]

            a_miss = (a is None)
            b_miss = (b is None)

            if a_miss ^ b_miss:
                if a_miss:
                    row1[c] = round(100 - b, 1)
                else:
                    row2[c] = round(100 - a, 1)






if __name__ == '__main__':
    # Loeme andmeid sisse
    data = []
    data = get_data(data, 'data/ETU41_20260216-171023.csv')
    clean_data(data)

    OUTPUT_DIR = "output_after_data_cleaning"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df = pd.DataFrame(data[2:], columns=data[1])


    # Täidame puuduvad väärtused
    fill_by_100_rule(
        data, df,
        ["Aasta", "Taustatunnus", "Sugu"],
        "Depressioon",
        ["Olulise depressioonita", "Olulise depressiooniga"]
    )

    fill_by_100_rule(
        data, df,
        ["Aasta", "Taustatunnus", "Depressioon"],
        "Sugu",
        ["Mehed", "Naised"]
    )

    df = pd.DataFrame(data[2:], columns=data[1])

    # Salvestame csv
    file_path2 = os.path.join(OUTPUT_DIR, "depression_cleaned_data.csv")

    with open(file_path2, mode="w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(data[1])
        writer.writerows(data[2:] )
