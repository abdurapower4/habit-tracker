from db_connection import Database
from datetime import datetime

class Tasks:
    """
    This Task objects it is responsible for creating, updating and deleting talks
    
    """
    # def __init__(self):
    #     self.conn
    #     self.duration
        
        
    def create_task(self,task,duration):
        db_conn = Database()
        conn = db_conn.connection()
        query = "INSERT INTO Tasks(Task,Days) VALUES(%s,%s)"
        data = (task,duration)
        save = conn.cursor()
        save.execute(query, data)
        conn.commit()
        
        print(save.rowcount,"Task created successfully")
        
    def get_tasks():
        db_conn = Database()
        conn = db_conn.connection()
        query = "SELECT * FROM Tasks"
        fetch = conn.cursor()
        fetch.execute(query)
        results = fetch.fetchall();
        return results
    
    def get_task(id):
        db_conn = Database()
        conn = db_conn.connection()
        query = "SELECT * FROM Tasks WHERE id = %s"
        data = (id,)
        fetch = conn.cursor()
        fetch.execute(query, data)
        results = fetch.fetchone();
        return results
    
    def set_dateCompleted(day,id,status):
        db_conn = Database()
        conn = db_conn.connection()
        query = "INSERT INTO Schedule(Task,{}) VALUES(%s,%s)".format(day);
        data = (id,status,)
        fetch = conn.cursor()
        fetch.execute(query, data)
        
        conn.commit()
        
    def not_ontrack(id):
        db_conn = Database()
        conn = db_conn.connection()
        query  = "UPDATE Tasks SET is_on_track = %s WHERE id = %s"
        data = ("No",id,)
        save = conn.cursor()
        save.execute(query, data)
        conn.commit()
        print(save.rowcount,"Task marked as complete successfully")
    
    def complete_task(id):
        date = datetime.now()
        db_conn = Database()
        conn = db_conn.connection()
        query  = "UPDATE Tasks SET Status = %s,dateCompleted = %s WHERE id = %s"
        data = ("Checked-Off",date,id,)
        save = conn.cursor()
        save.execute(query, data)
        conn.commit()
        print(save.rowcount,"Task marked as complete successfully")
        
    def delete_tasks(id):
        db_conn = Database()
        conn = db_conn.connection()
        query  = "DELETE  FROM Tasks WHERE id=%s"
        data = (id,)
        save = conn.cursor()
        save.execute(query, data)
        conn.commit()
        print(save.rowcount,"Task marked as deleted successfully")
        
    def all_daily_habits():
        db_conn = Database()
        conn = db_conn.connection()
        query = "SELECT * FROM Tasks WHERE Days = %s"
        data = ("Weekly",)
        fetch = conn.cursor()
        fetch.execute(query, data)
        results = fetch.fetchall();
        return results
    
    def longest_streak():
        db_conn = Database()
        conn = db_conn.connection()
        query = "SELECT Task, COUNT(*) AS count FROm Schedule GROUP BY Task ORDER BY count DESC LIMIT 1"
        fetch = conn.cursor()
        fetch.execute(query)
        results = fetch.fetchall();
        return results
    
    def least_streak():
        db_conn = Database()
        conn = db_conn.connection()
        query = "SELECT Task, COUNT(*) AS count FROm Schedule GROUP BY Task ORDER BY count ASC LIMIT 1"
        fetch = conn.cursor()
        fetch.execute(query)
        results = fetch.fetchall();
        return results
    
    def brocken_habits(status):
        db_conn = Database()
        conn = db_conn.connection()
        query = "SELECT * FROM Tasks WHERE is_on_track= %s"
        data = (status,)
        fetch = conn.cursor()
        fetch.execute(query, data)
        results = fetch.fetchall();
        return results