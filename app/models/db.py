import mysql.connector

conn = mysql.connector.connect(
    host='monorail.proxy.rlwy.net',
    port=40700,
    user='railway',
    password='02PPDKfP6JO6f4tuTwt1Ve7WLYwU1im-',
    database='railway'
)

cursor = conn.cursor()