import mysql.connector
import information as inf


class DbStuff:
    def __init__(self):
        # self.val = val
        self.mysql_create_db = "CREATE DATABASE IF NOT EXISTS netcourse"
        self.mysql_create_table = "CREATE TABLE IF NOT EXISTS gameinfo (Id INT AUTO_INCREMENT PRIMARY KEY, ip VARCHAR(200))"
        self.mysql_insert_into = "INSERT INTO gameinfo (ip) VALUES ('{}')"

    def connect_db(self, val):
        ip_val = val
        try:
            db = mysql.connector.connect(
                host=inf.HOST,
                user=inf.USER,
                passwd=inf.PASSWORD,
                database="netcourse"
            )

            if db.is_connected():
                db_info = db.get_server_info()
                print(db_info)
                cursor = db.cursor()
                cursor.execute(self.mysql_create_table)

                if val != "":
                    cursor.execute(self.mysql_insert_into.format(ip_val))
                    print("Insert ", cursor)

            db.commit()

        except mysql.connector.Error as e:
            print("Error connecting: ", e)

        finally:
            if db.is_connected():
                cursor.close()
                db.close()
                print("connection closed")
