from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

db = mysql.connector.connect(
    host="172.104.234.95",
    user=os.getenv("DBUSER"),
    passwd=os.getenv("DBPASSWD"),
    database="netcourse"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS first ("
                 "id int PRIMARY KEY AUTO_INCREMENT,"
                 "name VARCHAR(50))")

mycursor.execute("INSERT INTO first (name) VALUES ('Hans2')")
db.commit()
mycursor.execute("SELECT * FROM first")
for x in mycursor:
    print(x)
