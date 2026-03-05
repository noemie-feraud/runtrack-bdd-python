import mysql.connector
import pandas as pd

# Connexion à MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="pr4M369w!",
    database="LaPlateforme"
)

data = "SELECT * FROM LaDlateforme.etudiant"
df = pd.read_sql(data, conn)
print(df)

if conn.is_connected():
    print("Connexion réussi à MySQL !")

conn.close()

