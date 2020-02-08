import pymysql
import os

class Database:
    def __init__(self):
        self.connection = pymysql.connect(host="localhost",user="jomirosn_jomi",  password= os.environ['DB_PASSWORD'], db = 'jomirosn_aep_database', cursorclass=pymysql.cursors.DictCursor, port = int(os.environ['MYSQL_PORT_NUMBER']))    

    def verify(self, username, password):
        
        with self.connection.cursor() as cursor:

            sql = "SELECT `username`, `password` FROM `users` WHERE `username`=%s AND `password`=%s"
            cursor.execute(sql, (username, password, ))
            result = cursor.fetchone()

            if result:
                return result
            else: 
                return None

    def insert_data(self, data):
        """
            data - list of dictionary entries
             ex: [{'station_number': "1_sample", ...}, {'station_number': "1_sample", ...}]
        """

        sql_data_bulk = ''

        for i in range(0,len(data)):
            data_key = ''
            data_value = ''

            for key,value in data[i].items():
                if key == 'station_number':
                    data_key += key + ","
                    data_value += "\"" + value + "\"" + ","

                elif value == 'NAN':
                    data_key += key + ","
                    data_value += "0" + ","
                else:
                    data_key += key + ","
                    data_value += value + ","

            sql_column = data_key[0:len(data_key)-1]
            sql_data = "(" + data_value[0:len(data_value)-1] + ")"
            
            sql_data_bulk += sql_data + ","
        
        
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO data ({0}) VALUES {1};".format(sql_column, sql_data_bulk[0:len(sql_data_bulk)-1]) 
            cursor.execute(sql)

        return ''
