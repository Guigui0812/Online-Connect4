import mysql

class StaticsDatabase:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="mydatabase"
        )

    def record_stats(self, statistics):
        # Ici on va faire différentes requêtes pour stocker les informations que l'on recevra en fin de partie
        # On reçoit les stats sous forme de dictionnary
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM customers")
        myresult = mycursor.fetchall()