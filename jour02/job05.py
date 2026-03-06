import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "pr4M369w!",
    database = "LaPlateforme"
)

cursor = connection.cursor()
cursor.execute("SELECT SUM(superfie) FROM etage")
resultat = cursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {resultat} m2")

cursor.close()
connection.close()
