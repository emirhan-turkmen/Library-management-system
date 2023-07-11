import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(
    host='localhost',
    database='testdb3',
    user='root',
    password='1')