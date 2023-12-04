# database/db.py
import cx_Oracle
from config import db_config

class Oracledb:
    def __init__(self):
        
        self.conn = cx_Oracle.connect(**db_config)
        self.cursor = self.conn.cursor()

    def birth(self, birth):
            from datetime import datetime
            try:
                datetime.strptime(birth, '%Y-%m-%d')
                string = f"to_date('{birth}', 'yyyy-mm-dd')"
                return string
            except ValueError:
                print("fail")
                return None

    def select(self, query, size):
        self.cursor.execute(query)
        return self.cursor.fetchmany(size)
    
    def selectpage(self, query, size, page):
        self.cursor.execute(query)
        data = self.cursor.fetchmany()
        total_count = len(data)
        page = int(page)
        total_pages = (total_count // size) + (1 if total_count % size > 0 else 0)
        start_idx = (page - 1) * size
        end_idx = start_idx + size
        print(start_idx, end_idx)
        result = data[start_idx: end_idx+1]
        return total_pages, result
        
    
    def selectall(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchmany()

    def authenticate_user(self, userid, password):
        query = f"SELECT count(*) FROM CUSTOMER WHERE Customer_ID='{userid}' AND Password='{password}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] > 0
    
    def authenticate_manager(self, id, name):
        query = f"SELECT count(*) FROM manager WHERE Manager_ID ='{id}' AND Name='{name}'"
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
    
        def insert(info): #signup
            try:
                self.conn.begin() 
                query = f"INSERT INTO CUSTOMER VALUES('{info[0]}', '{info[1]}','{info[2]}', '{info[3]}', {self.birth(info[4])}, '{info[5]}')"
                self.cursor.execute(query)
                self.conn.commit() # commit 
                return True
            except Exception as e: #transaction rollback
                self.conn.rollback()
                print(f"Error during insert: {e}")
                return False
            
        if isiddup(info[0]):
            if self.birth(info[4]) != None:
                return insert(info)
            else: 
                print('invalid birth')
        else:
            print('duplicate id')
            
        return False
    


    def order_insert(self, info):
        try:
            self.conn.begin() 
            query = f"INSERT INTO ORDERS VALUES('{info[0]}', '{info[1]}','{info[2][0]}', {self.birth(info[3])})"
            print(query)
            self.cursor.execute(query)
            self.conn.commit() # commit 
            return True
        except Exception as e: #transaction rollback
                self.conn.rollback()
                print(f"Error during insert: {e}")
                return False
        
    def ICB_insert(self, info):
        try:
            self.conn.begin() 
            query = f"INSERT INTO IS_CONTAINED_BY VALUES('{info[0]}', '{info[1]}',{info[2]}, {info[3]})"
            print(query)
            self.cursor.execute(query)
            self.conn.commit() # commit 
            return True
        except Exception as e: #transaction rollback
            self.conn.rollback()
            print(f"Error during insert: {e}")
            return False
        
    def notice_insert(self, info):
        try:
            self.conn.begin() 
            print("insert info")
            query = f"INSERT INTO NOTICE VALUES('{info[0]}', '{info[1]}',{self.birth(info[2])}, '{info[3]}')"
            print(query)
            self.cursor.execute(query)
            self.conn.commit() # commit 
            return True
        except Exception as e: #transaction rollback
            self.conn.rollback()
            print(f"Error during insert: {e}")
            return False
        
    def notice_delete(self, noticeid, managerid):
        try:
            query = f"DELETE FROM Manages WHERE Notice_ID='{noticeid}'and Manager_ID = {managerid}"
            self.cursor.execute(query)
            self.conn.commit()
            query = f"DELETE FROM NOTICE WHERE Notice_ID='{noticeid}'"
            self.cursor.execute(query)
            self.conn.commit()

        except Exception as e:
            print(f"Error: {e}")
            self.cursor.execute("ROLLBACK")
               

        

        
    def alcoholinfo(self, name):
        query = f"select taste, Alcohol_ID from alcohol where Name= '{name}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        print(result)
        return result

        
    def search(self, info):
        #info : [beer_type, beer_name, minprice, maxprice, star]
        # lower(A.Type) NOT IN {l} 
        l = "('soju', 'beer', 'makgeolli', 'wine', 'sake', 'whiskey', 'tequila', 'brandy', 'gin', 'rum')"
        wherequery = []
        print(info)
        if info[0] == 'etc':
            wherequery.append(f"lower(A.type) not in {l}")
        elif info[0].lower() != 'all':
            info[0].lower()
            wherequery.append(f"lower(A.type) = '{info[0].lower()}'")
        
        if len(info[1]) != 0:
            info[1].lower()
            wherequery.append(f"lower(A.Name) like '%{info[1]}%'")

        if len(info[2]) == 0:
            info[2] = 0
        if len(info[3]) == 0:
            info[3] = 100000000
        
        wherequery.append(f"A.Price between {info[2]} and {info[3]}")
        if info[4] == None:
            info[4] = 1
        wherequery.append(f"P.Star_rating >= {info[4]}")
        wq = ""
        if len(wherequery) > 0:
            wq = wherequery[0]
            for x in wherequery[1:]:
                wq += " AND "
                wq += x

        query = f"SELECT A.Name, A.Price, A.Alcohol_degree, A.Type, round(avg(P.Star_rating),1), A.Alcohol_ID,  A.Picture FROM ALCOHOL A, POINT P WHERE A.Alcohol_ID=P.Alcohol_ID and "+wq+" group by A.Name, A.Price, A.Alcohol_degree, A.Type, A.Alcohol_ID, A.Picture order by DBMS_RANDOM.VALUE"
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchmany()
        #print(result)
        return result
    
    def close_db(self):
        self.cursor.close()
