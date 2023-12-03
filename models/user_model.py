# models/user_model.py
class User:
    def __init__(self):
        self.userid = None
        self.phonenum = None
        self.name = None
        self.birth = None
        self.address = None

    def get_current_user_info(self):
        self.userid = session['userid']
        info = oracle.get_user_info(self.userid)
        self.name = info[2]
        self.phonenum = info[3]
        self.birth = info[4]
        self.address = info[5]
        return self.userid
