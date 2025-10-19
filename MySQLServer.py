import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server (update credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password'   # 🔹 Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Ensure connection is closed safely
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()
