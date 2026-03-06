import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="pr4M369w!",
    database="LaPlateforme"
)

cursor = connection.cursor()
cursor.execute("SELECT nom, capacite FROM salle")
resultats = cursor.fetchall()
print(resultats)

cursor.close()
connection.close()

