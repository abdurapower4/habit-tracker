import mysql.connector
"""
This is a database connection class,
we set user,host,password and database name
"""
class Database:
    def __init__(self):
        self.user = "root"
        self.password = ""
        self.host = "127.0.0.1"
        self.database = "TaskTracker"
        
    def connection(self):
        conn = mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            database = self.database
        )
        return conn