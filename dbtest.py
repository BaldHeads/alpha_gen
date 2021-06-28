import libs.db as db
import sqlite3

db_file = "sp10_not_normalized.db"

conn = db.create_connection(db_file)
sql = "SELECT COUNT(*) FROM historical"
cur = conn.cursor()
cur.execute(sql)
for row in cur:
    print(row)

db.close_connection(conn)
