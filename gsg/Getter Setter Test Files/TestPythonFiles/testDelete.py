import sqlite3
conn = sqlite3.connect("webtech.db")
cur = conn.cursor()
query = """
            select title, text, id, user, email, homepage
            from users, text_messages
            where title==title and user==user;
"""
cur.execute(query)
for row in cur.fetchall():
        print(row[0],row[1],row[2],row[3],row[4],row[5])
