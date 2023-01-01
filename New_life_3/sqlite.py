import sqlite3 as sq


class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_profile(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
            return bool(len(result))
    # if not user:
    #     cur.execute("INSERT INTO profile VALUES(?);", (user_id))
    #     db.commit()

    def edit_profile(self, user_id,):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES(?)", (user_id,))

    def local(self, location):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('location') VALUES(?)", (location,))

    def check_city_user(self, city):
        with self.connection:
            speed = self.cursor.execute("SELECT * FROM 'users' WHERE 'city' = ?", (city,)).fetchmany(1)
            return bool(len(speed))

    def city_user(self, city):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('city') VALUES(?)", (city,))

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id, ))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users").fetchall()
