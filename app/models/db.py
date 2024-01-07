import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    database='timesjournal'
)

cursor = conn.cursor()