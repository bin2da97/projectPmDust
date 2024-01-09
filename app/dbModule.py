import MySQLdb

class Database():
    def __init__(self):
        self.db = MySQLdb.connect(host='localhost',
                                  user='root',
                                  password='1234',
                                  db='project3',
                                  charset='utf8')
        self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)

    def execute(self, query, args=None):
        self.cursor.execute(query, args)
        return self.cursor

    def commit(self):
        self.db.commit()

    def fetchone(self):
        result = self.cursor.fetchone()
        return result

    def fetchall(self):
        result = self.cursor.fetchall()
        return result



