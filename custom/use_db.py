import psycopg2


class UseDB():
    def connect_db():
        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cursor = conn.cursor()
        return conn, cursor

    def all_users():
        sql = 'select Name from random_user'
        users = []
        conn, cursor = connect_db()
        cursor.execute(sql)
        records = cursor.fetchall()
        for user in records:
            users.append(user[0])
        return users

    def insert_user(insert_username):
        sql = 'insert into random_user (Name) values(\'' + str(
            insert_username) + '\')'
        conn, cursor = connect_db()
        cursor.execute(sql)
        conn.commit()

    def delete_user(delete_username):
        sql = 'delete from random_user where Name = \'' + str(
            delete_username) + '\''
        conn, cursor = connect_db()
        cursor.execute(sql)
        conn.commit()