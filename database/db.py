# database/db.py
import cx_Oracle

class Oracledb:
    def __init__(self):
        db_config = {
            'user': 'alcohol',
            'password': 'comp322',
        }
        self.conn = cx_Oracle.connect(**db_config)
        self.cursor = self.conn.cursor()

    def select(self, query, size):
        self.cursor.execute(query)
        return self.cursor.fetchmany(size)

    def authenticate_user(self, userid, password):
        query = f"SELECT count(*) FROM CUSTOMER WHERE Customer_ID='{userid}' AND Password='{password}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] > 0

    def get_user_info(self, userid):
        query = f"SELECT * FROM CUSTOMER WHERE Customer_ID = '{userid}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
    
    def signup(self, info):
        def isiddup(id):
            query = f"SELECT COUNT(*) FROM CUSTOMER WHERE Customer_ID ='{id}'"
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result[0] == 0
        
        def birth(birth):
            from datetime import datetime
            try:
                datetime.strptime(birth, '%Y-%m-%d')
                string = f"to_date('{birth}', 'yyyy-mm-dd')"
                return string
            except ValueError:
                print("fail")
                return None
        
        def insert(info):
            try:
                self.conn.begin() 
                query = f"INSERT INTO CUSTOMER VALUES('{info[0]}', '{info[1]}','{info[2]}', '{info[3]}', {birth(info[4])}, '{info[5]}')"
                self.cursor.execute(query)
                self.conn.commit() # commit 
                return True
            except Exception as e: #transaction rollback
                self.conn.rollback()
                print(f"Error during insert: {e}")
                return False
            
        
        if isiddup(info[0]):
            if birth(info[4]) != None:
                return insert(info)
            else: 
                print('invalid birth')
        else:
            print('duplicate id')
            
        return False
    
    def close_db(self):
        self.cursor.close()
