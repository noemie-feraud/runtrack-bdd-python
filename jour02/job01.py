import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "pr4M369w!",
    database = "LaPlateforme"
)

data = "SELECT * FROM etudiant"
df = pd.read_sql(data, connection)
print(df)

connection.close()