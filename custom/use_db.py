import psycopg2


class UseDB():
    def __init__(self):
        pass
        
    def connect_db(self):
        # DATABASE_URL = os.environ['DATABASE_URL']
        # conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        # cursor = conn.cursor()
        conn, cursor = [1,2,3],[4,5,6]
        return conn, cursor

    def all_users(self):
        sql = 'select Name from random_user'
        users = []
        conn, cursor = self.connect_db()
        # cursor.execute(sql)
        # records = cursor.fetchall()
        # for user in records:
        #     users.append(user[0])
        # return users
        return cursor

    def insert_user(self, insert_username):
        sql = 'insert into random_user (Name) values(\'' + str(
            insert_username) + '\')'
        conn, cursor = self.connect_db()
        cursor.execute(sql)
        conn.commit()

    def delete_user(self, delete_username):
        sql = 'delete from random_user where Name = \'' + str(
            delete_username) + '\''
        conn, cursor = self.connect_db()
        cursor.execute(sql)
        conn.commit()