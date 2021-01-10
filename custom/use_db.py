import psycopg2
from psycopg2 import sql
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
        sql_string = 'select Name from random_user'
        users = []
        conn, cursor = self.connect_db()
        cursor.execute(sql_string)
        records = cursor.fetchall()
        for user in records:
            users.append(user[0])
        return users

    def insert_user(self, insert_username):
        conn, cursor = self.connect_db()
        cursor.execute(sql.SQL("insert into random_user (Name) values(%s)"), [
            insert_username,
        ])
        conn.commit()

    def delete_user(self, delete_username):
        conn, cursor = self.connect_db()
        cursor.execute(sql.SQL("delete from random_user where Name = %s"), [
            delete_username,
        ])
        conn.commit()