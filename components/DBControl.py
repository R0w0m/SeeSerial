import sqlite3


class DBControl:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(f"data/{self.db_name}")
        self.cursor = self.conn.cursor()

        self.create_table(
            "serial",
            "id INTEGER PRIMARY KEY AUTOINCREMENT, \
            name TEXT, \
            path TEXT, \
            note TEXT, \
            image_path TEXT, \
            favorite INTEGER DEFAULT 0",
        )
        self.create_table(
            "season",
            "id INTEGER PRIMARY KEY AUTOINCREMENT, \
            serial_id INTEGER, \
            name TEXT, \
            path TEXT",
        )
        self.create_table(
            "episode",
            "id INTEGER PRIMARY KEY AUTOINCREMENT, \
            parent_id INTEGER, \
            parent_type INTEGER, \
            name TEXT, \
            path TEXT, \
            position INTEGER, \
            pos_percent INTEGER",
        )
        self.create_table(
            "settings",
            "name TEXT PRIMARY KEY, \
            value INTEGER",
        )
        self.init_settings()


    def init_settings(self):
        settings = (
            ("is_dark", 0),
            ("color", 0),
            ("is_fullscreen", 0),
            ("is_autoplay", 0),
            ("is_repeat", 0),
        )
        
        self.cursor.execute("SELECT COUNT(*) FROM settings")
        count = self.cursor.fetchone()[0]

        if count == 0:
            self.cursor.executemany("INSERT INTO settings (name, value) VALUES (?, ?)", settings)
            self.conn.commit()

    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert(self, table_name, columns, values):
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.conn.commit()

    def insert_(self, table_name, columns, values):
        req = (
            f"INSERT INTO {table_name} ({columns}) VALUES ("
            + "?, " * (len(values) - 1)
            + "?)"
        )
        self.cursor.execute(req, values)
        self.conn.commit()

    def insert_ep(self, table_name, columns, name: str, path: str, parent_id: int):
        vals = (name, path, parent_id)
        self.cursor.execute(
            """INSERT INTO episode (name, path, parent_id) VALUES (?, ?, ?)""", vals
        )
        self.conn.commit()

    def select(self, table_name, columns, where=""):
        if where == "":
            self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        else:
            self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {where}")
        return self.cursor.fetchall()

    def update(self, table_name, val, where):
        self.cursor.execute(f"UPDATE {table_name} SET {val} WHERE {where}")
        self.conn.commit()

    def delete(self, table_name, where):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {where}")
        self.conn.commit()

    def drop(self):
        self.cursor.execute("DROP DATABASE IF EXISTS " + self.db_name)
        self.conn.commit()

    def request(self, req):
        self.cursor.execute(req)
        self.conn.commit()

    # select all tables with their contents and print them
    def print_db(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cursor.fetchall()
        for table_name in tables:
            self.beautiuful_print(table_name[0])

    def beautiuful_print(self, table_name):
        self.cursor.execute("SELECT * FROM " + table_name)
        print(self.cursor.fetchall())

    def close(self):
        self.conn.close()


class DBUsers(DBControl):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.create_table(
            "user",
            "id INTEGER PRIMARY KEY AUTOINCREMENT, \
            name TEXT, \
            password TEXT",
        )

    def insert_user(self, name: str, password: str):
        vals = (name, password)
        self.cursor.execute(
            """INSERT INTO user (name, password) VALUES (?, ?)""", vals
        )
        self.conn.commit()

    def select_user(self, name: str):
        self.cursor.execute(f"SELECT * FROM user WHERE name = '{name}'")
        return self.cursor.fetchall()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM user")
        return self.cursor.fetchall()

    def select_user_id(self, id: int):
        self.cursor.execute(f"SELECT * FROM user WHERE id = {id}")
        return self.cursor.fetchall()

    def get_password(self, id: int):
        self.cursor.execute(f"SELECT password FROM user WHERE id = {id}")
        return self.cursor.fetchall()

    def update_user(self, name: str, password: str):
        self.cursor.execute(
            f"UPDATE user SET password = '{password}' WHERE name = '{name}'"
        )
        self.conn.commit()

    def delete_user(self, name: str):
        self.cursor.execute(f"DELETE FROM user WHERE name = '{name}'")
        self.conn.commit()
