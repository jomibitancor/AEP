import pymysql
import os

class Database:
    def __init__(self):
        self.connection = pymysql.connect(host="localhost",user="jomirosn_jomi",  password= os.environ['DB_PASSWORD'], db = 'jomirosn_aep_database', cursorclass=pymysql.cursors.DictCursor)    

    def verify(self, username, password):
        
        with self.connection.cursor() as cursor:

            sql = "SELECT `username`, `password` FROM `users` WHERE `username`=%s AND `password`=%s"
            cursor.execute(sql, (self.username, self.password, ))
            result = cursor.fetchone()

            if result:
                return result
            else: 
                return None

db = Database()
