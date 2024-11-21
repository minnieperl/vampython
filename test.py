import mysql.connector

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # replace with your MySQL username
            password='7907',  # replace with your MySQL password
            database='hotel_booking'  # replace with your database name
        )
        print("Connection successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create a table for hotel bookings
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),check_in DATE,check_out DATE,room_type VARCHAR(50)
            )
        """)
        connection.commit()
        print("Table created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# Insert booking data

def insert_booking(connection, name, check_in, check_out, room_type, booking_number):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO bookings (name, check_in, check_out, room_type)
            VALUES (%s, %s, %s, %s)
        """, (name, check_in, check_out, room_type))
        connection.commit()
        print(f"Booking {booking_number} inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def main():
    connection = connect_to_database()
    if connection:
        # Sample user data
        bookings = [
            ("Alice", "2024-11-20", "2024-11-25", "Single"),
            ("Bob", "2024-11-21", "2024-11-23", "Double"),
            ("Charlie", "2024-11-22", "2024-11-26", "Suite"),
            ("David", "2024-11-20", "2024-11-22", "Single"),
            ("Eva", "2024-11-25", "2024-11-30", "Double"),
        ]

        # Insert sample bookings into the database
        for i, booking in enumerate(bookings, start=1):  # start=1 to number bookings starting from 1
            insert_booking(connection, *booking, booking_number=i)

        print("All bookings have been successfully added to the database.")

        # Close the database connection
        connection.close()


if __name__ == "__main__":  
    main()
