import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "pr4M369w!" ,
    database = "LaPlateforme"
)

data1 = "SELECT * FROM LaPlateforme.etage "
df1 = pd.read_sql(data1, connection)

data2 = "SELECT * FROM LaPlateforme.salle"
df2 = pd.read_sql(data2, connection)

print("--- DATAFRAME ETAGE ---")
print(df1)

print("--- DATAFRAME SALLE ---")
print(df2)

connection.close()