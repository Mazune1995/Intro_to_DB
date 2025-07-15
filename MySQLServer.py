#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (change user & password as needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password_here'  # Replace with your MySQL root password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Cleanup: Close cursor and connection if they were opened
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

