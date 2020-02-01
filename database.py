import pymysql

class Database:
    def __init__(self, username, password):
        self.connection = pymysql.connect(host="localhost",user="jomirosn_jomi",  password= os.environ['DB_PASSWORD'], db = 'jomirosn_aep_database', cursorclass=pymysql.cursors.DictCursor)
        self.username = username
        self.password = password

    def verify(self):
        
        with self.connection.cursor() as cursor:
            try:
                sql = "SELECT `username` FROM `users` WHERE `username`=%s"
                cursor.execute(sql, (self.username,))
                result = cursor.fetchone()
                return result

            except:
                return 'User does not exist'


,