import sqlite3


def minimal_create_database():
    """The minimal commands to create a database"""
    conn = sqlite3.connect('data/patent_npi_db.sqlite')
    cursor = conn.cursor()  # optional
    cursor.close()  # optional


def create_database():
    """Create a new sqlite database"""
    query = """
    CREATE TABLE patents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(250) NOT NULL
    );
    """
    # Connection is the connection to the database rather than the
    # database itself
    conn = sqlite3.connect('data/patent_npi_db.sqlite') # who you're messaging
    cursor = conn.cursor()  # a new text chain/instagram/snapchat story
    cursor.execute(query)  # posting

    # SELECT pulls back information
    cursor.execute('SELECT sqlite_version();')  # open story, adding message, reading comments
    record = cursor.fetchall()  # pulling back all posts in conversation (but we've only asked for 1)
    print(record)  # look at the output (which should be a list of length 1)
    cursor.close()  # close the story


if __name__ == '__main__':
    create_database()