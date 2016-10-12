# Using SQLite3 & Python

# connect to database
import sqlite3
from sqlite3 import dbapi2 as sqlite
conn  = sqlite.connect("test.db")


# create cursor to issue queries
#cur = conn.cursor()

# the below is using Pysqlite
conn.row_factory = sqlite.Row


cur = conn.execute("select first, last, age from user;")

# generate table
print ("<table>")
print "<tr><th>First</th><th>Last</th><th>Age</th></tr>"
for row in cur.fetchall():
    print ("<tr><td>", row[0], "</td><td>", row[1], "</td><td>", row[2], "</td></tr>")
print "</table>"   
    
