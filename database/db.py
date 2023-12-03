# database/db.py
import cx_Oracle

class Oracledb:
    def __init__(self):
        db_config = {
            'user': 'alcohol',
            'password': 'comp322',
        }
        conn = cx_Oracle.connect(**db_config)
        self.cursor = conn.cursor()

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

    def close_db(self):
        self.cursor.close()
