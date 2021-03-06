import MySQLdb


class Database:

    host = 'localhost'
    user = 'root'
    password = ''
    db = 'python_restful'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":

    db = Database()

    #CleanUp Operation
    del_query = "DELETE FROM messages"
    db.insert(del_query)

    # Data Insert into the table
    query = """
        INSERT INTO messages
        (`body`, `created_at`)
        VALUES
        ('Hi', '2017-08-28 00:00:00'),
        ('Hello', '2017-08-28 00:00:00'),
        ('Take a rest', '2017-08-28 00:00:00')
        """

    # db.query(query)
    db.insert(query)

    # Data retrieved from the table
    select_query = """
        SELECT * FROM messages
        WHERE body = 'Hi'
        """

    people = db.query(select_query)

    for person in people:
        print "Found %s " % person['body']