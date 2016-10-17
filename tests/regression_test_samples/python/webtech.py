# Example Database COMP249 -- 2010


import sqlite3
import hashlib
import sys
import os


dblocation = "./"
dbname = 'webtech.db'


def connect():
    conn = sqlite3.connect(dblocation+dbname)
    return conn


def init():

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("DROP TABLE users")
        cur.execute("DROP TABLE sessions")
        cur.execute("DROP TABLE text_messages")
    except:
        pass
     
    cur.execute("""
      CREATE TABLE users (
        email VARCHAR NOT NULL PRIMARY KEY,  
        fullname VARCHAR,
        country VARCHAR,
        homepage VARCHAR,
        password VARCHAR )""")

    cur.execute("""
      CREATE TABLE text_messages (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user VARCHAR, 
        title VARCHAR, 
        text VARCHAR,  
        date VARCHAR DEFAULT CURRENT_TIMESTAMP )""")

    cur.execute("""
      CREATE TABLE sessions (
        sessionid VARCHAR NOT NULL PRIMARY KEY,
        user VARCHAR ) """)

    conn.commit()


def pwcrypt(string):
    return hashlib.sha1(string).hexdigest()


def sample_data():
    
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO users VALUES \
      ('jim@there.com', 'Jim', 'Australia', 'http://www.google.com/', ?)", \
                (pwcrypt('jim'),))
    
    cur.execute("INSERT INTO users VALUES \
      ('bob@here.com', 'Bob', 'Austria', 'http://www.yahoo.com/', ? )", \
                (pwcrypt('bob'),))
    
    emails   = ['jim@there.com', 'bob@here.com']
    
    messages = (('COMP249', 'Some text about COMP249 ...'),
               ('COMP348', 'Some text about COMP348 ...'),
               ('Britney Spears', 'Some text about Britney Spears ...'),
               ('Leonard Cohen', 'Some text about Leonard Cohen ...'),
               ('Kevin Rudd', 'Some text about Kevin Rudd ...'),
               ('Lara Bingle', 'Some text about Lara Bingle ...'))

    for email in emails:
        for title, text in messages:
            
            cur.execute("INSERT INTO text_messages \
              (user, title, text) VALUES (?,?,?)", (email, title, text))
            
            conn.commit()
            
            cur.execute("SELECT id FROM text_messages \
               WHERE user=? AND title=?", (email, title))
            
            result = cur.fetchone()
            
            if result != None:
                text_message_ID = result[0]
            else:
                print "Problem storing text messages"
                sys.exit()
        
    conn.commit()

    
if __name__=='__main__':
    print "Initialising database tables ..."
    init()
    print "Creating sample data ..."
    sample_data()
    print "Done."
    

