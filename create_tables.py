from db_connection import Database


def create_tables():
    try:
        db_conn = Database()
        conn = db_conn.connection()
        query = "CREATE TABLE Tasks (id INT PRIMARY KEY AUTO_INCREMENT,Task VARCHAR(255),Status VARCHAR(300),Days VARCHAR(300),is_on_track VARCHAR(10) NOT NULL DEFAULT 'yes',dateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP,dateCompleted VARCHAR(300) NULL)"
        
        fetch = conn.cursor()
        fetch.execute(query)
        # conn.commit()
        print("Table Tasks created successfully");
    except Exception as e:
        print("Error creating table:", e)
    
def create_schedule_table():
    try:
        db_conn = Database()
        conn = db_conn.connection()
        query = "CREATE TABLE Schedule (id INT PRIMARY KEY AUTO_INCREMENT,Task INT NOT NULL,Monday VARCHAR(300) NULL,Tuesday VARCHAR(300) NULL,Wednesday VARCHAR(300) NULL,Thursday VARCHAR(300) NULL,Friday VARCHAR(300) NULL,Saturday VARCHAR(300) NULL,Sunday VARCHAR(300) NULL,FOREIGN KEY (Task) REFERENCES Tasks(id))"
        
        fetch = conn.cursor()
        fetch.execute(query)
        # conn.commit()
        print("Table Schedule created successfully");
    except Exception as e:
        print("Error creating table:", e)
        
        
create_tables()
create_schedule_table()