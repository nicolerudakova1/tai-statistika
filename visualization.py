import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output_after_data_cleaning/depression_cleaned_data.csv")

year = 2019

education_groups = [
    "Põhiharidus või madalam",
    "Keskharidus",
    "Kõrgharidus"
]

filtered = df[
    (df["Aasta"] == year) &
    (df["Sugu"] == "Mehed ja naised") &
    (df["Depressioon"] == "Olulise depressiooniga") &
    (df["Taustatunnus"].isin(education_groups))
]

age_cols = df.columns[4:]

plt.figure()

for edu in education_groups:
    row = filtered[filtered["Taustatunnus"] == edu].iloc[0]
    plt.plot(age_cols, row[age_cols].values, label=edu)

plt.xlabel("Vanuserühm")
plt.ylabel("Depressioon (%)")
plt.title(f"Olulise depressiooniga hariduse järgi ({year})")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()
