import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "pr4M369w!",
    database = "LaPlateforme"
)

cursor = connection.cursor()
cursor.execute("SELECT SUM(capacite) FROM salle")
resultat = cursor.fetchone()[0]
print(f"La capacité de toutes les salles est de : {resultat}")