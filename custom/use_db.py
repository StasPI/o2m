import psycopg2
import os


class UseDB():
    def __init__(self):
        pass

    def connect_db(self):
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        return conn, cursor

    def all_users(self):
        sql = "select Name from random_user"
        users = []
        conn, cursor = self.connect_db()
        cursor.execute(sql)
        records = cursor.fetchall()
        for user in records:
            users.append(user[0])
        return users

    def insert_user(self, insert_username):
        sql = "insert into random_user (Name) values(%s')"
        conn, cursor = self.connect_db()
        cursor.execute(sql, (insert_username, ))
        conn.commit()

    def delete_user(self, delete_username):
        sql = "delete from random_user where Name =%s'"
        conn, cursor = self.connect_db()
        cursor.execute(sql, (delete_username, ))
        conn.commit()