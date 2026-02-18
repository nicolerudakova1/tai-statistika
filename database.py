import sqlite3
import pandas as pd


df = pd.read_csv("output_after_data_cleaning/depression_cleaned_data.csv")


conn = sqlite3.connect("depression.db")


df.to_sql("depression_stats", conn, if_exists="replace", index=False)


query1 = """SELECT Taustatunnus,
       "25-34" AS percent
FROM depression_stats
WHERE Aasta = 2019
  AND Sugu = 'Mehed ja naised'
  AND Depressioon = 'Olulise depressiooniga'
  AND Taustatunnus IN (
      'Põhiharidus või madalam',
      'Keskharidus',
      'Kõrgharidus'
  )
ORDER BY percent DESC;

"""

query2 = """
SELECT Taustatunnus, "25-34" AS percent
FROM depression_stats
WHERE Aasta = 2019
  AND Sugu = 'Mehed ja naised'
  AND Depressioon = 'Olulise depressiooniga'
  AND Taustatunnus IN ('Eestlane', 'Mitte-eestlane')
ORDER BY percent DESC;

"""
print("-------------1 päring------------------")
print(pd.read_sql(query1, conn))
print("-------------2 päring------------------")
print(pd.read_sql(query2, conn))

conn.close()
