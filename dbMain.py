from dotenv import load_dotenv
import mysql.connector
import os
import globals

load_dotenv()

db = mysql.connector.connect(
    host=globals.SERVER_ADR,
    user=os.getenv("DBUSER"),
    passwd=os.getenv("DBPASSWD")
)

mycursor = db.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS first (
                 id int PRIMARY KEY AUTO_INCREMENT,
                 name VARCHAR(50))""")

mycursor.execute("INSERT INTO first (name) VALUES ('Hans2')")
db.commit()
mycursor.execute("SELECT * FROM first")
for x in mycursor:
    print(x)
