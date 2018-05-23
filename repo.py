import sqlite3


class ToyRepo(object):
    DB_NAME = 'db/toys.db'

    def __init__(self):
        self.con = sqlite3.connect(ToyRepo.DB_NAME)
        with self.con as c:
            c.execute('CREATE TABLE IF NOT EXISTS toys (name text unique, price int, min_age int, max_age int)')

    def get_all(self):
        with self.con as c:
            return c.execute('SELECT rowid, * FROM toys').fetchall()

    def get_where(self, min_price, max_price, min_age, max_age):
        with self.con as c:
            return c.execute(
                'SELECT rowid, * FROM toys WHERE price >= ? AND price <= ? AND min_age >= ? AND max_age <= ?',
                (min_price, max_price, min_age, max_age)).fetchall()

    def put(self, name, price, min_age, max_age):
        with self.con as c:
            cur = c.cursor()
            cur.execute('INSERT OR REPLACE INTO toys VALUES (?, ?, ?, ?)', (name, price, min_age, max_age))
            return cur.lastrowid

    def remove(self, rowid):
        with self.con as c:
            c.execute('DELETE FROM toys WHERE rowid = ?', (rowid,))
