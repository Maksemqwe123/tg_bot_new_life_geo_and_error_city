import sqlite3 as sq


class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()
            # return bool(len(result))

    # if not user:
    #     cur.execute("INSERT INTO profile VALUES(?);", (user_id))
    #     db.commit()
    def edit_profile(self, city):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'use' VALUES(?)", (city,))

    def create_profile(self, city):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'use';", (city,))
            one_result = result.fetchone()
            print(one_result)

# import sqlite3
#
# conn = sqlite3.connect(r'C:\Program Files\db.base/der.db')
#
# cur = conn.cursor()
#
# cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     userid INT PRIMARY KEY,
#     fname TEXT,
#     lname TEXT,
#     gender TEXT
# );""")
#
# conn.commit()
#
#
# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
# conn.commit()
