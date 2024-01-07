import mysql.connector

conn = mysql.connector.connect(
    host='viaduct.proxy.rlwy.net',
    port=58384,
    user='railway',
    password='orH6IBKTa6CbtYioAuOs4AwNm~-i1.Z0',
    database='railway'
)

cursor = conn.cursor()