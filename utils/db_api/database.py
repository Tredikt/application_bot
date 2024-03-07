from sqlite3 import connect


class DataBase:
    def __init__(self, db_name):
        self.conn = connect(database=db_name)
        self.cur = self.conn.cursor()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                tg_id INTEGER PRIMARY KEY,
                phone TEXT,
                name TEXT,
                username TEXT
            )
            """
        )

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS admins(
                tg_id INTEGER
            )
            """
        )

        self.conn.commit()

    def add_user(self, tg_id, phone, name, username):
        self.cur.execute(
            """
            INSERT OR REPLACE INTO users
            (tg_id, phone, name, username)
            VALUES
            (?, ?, ?, ?)
            """,
            (tg_id, phone, name, username)
        )
        self.conn.commit()

    def get_users_ids(self) -> list:
        users_id = self.cur.execute(
            """
            SELECT tg_id FROM users
            """
        ).fetchall()

        return [] if users_id is None else [elem[0] for elem in users_id]

    def get_user_data(self, tg_id: int) -> tuple:
        user_data = self.cur.execute(
            f"""
            SELECT name, phone, username FROM users
            WHERE tg_id = {tg_id}
            """
        ).fetchone()

        return user_data

    def add_admin(self, tg_id: int):
        self.cur.execute(
            """
            INSERT OR REPLACE INTO admins
            (tg_id)
            VALUES
            (?)
            """,
            (tg_id, )
        )

        self.conn.commit()

    def get_admins(self):
        admins = self.cur.execute(
            """
            SELECT tg_id FROM admins
            """
        ).fetchall()

        return [elem[0] for elem in admins] if admins else []