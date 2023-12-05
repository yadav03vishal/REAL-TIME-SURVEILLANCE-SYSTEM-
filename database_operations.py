# database_operations.py

import sqlite3

def create_database():
    conn = sqlite3.connect('batch_info.db')
    cursor = conn.cursor()

    # Create the batch_info table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS batch_info (
            batch_id INTEGER PRIMARY KEY,
            starting_frame_id INTEGER,
            ending_frame_id INTEGER,
            timestamp INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def insert_batch_info(batches):
    conn = sqlite3.connect('batch_info.db')
    cursor = conn.cursor()

    for batch in batches:
        cursor.execute('''
            INSERT INTO batch_info (timestamp)
            VALUES (?)
        ''', (batch['timestamp'],))

    conn.commit()
    conn.close()


# Example usage
def main():
    # Assuming you have retrieved batches from user_interaction.py
    example_batches = [
        {'batch_id': 1, 'starting_frame_id': 1, 'ending_frame_id': 25, 'timestamp': 1638806820},
        # Add more batches as needed
    ]

    # Initialize the database (run this only once)
    create_database()

    # Insert batch information into the database
    insert_batch_info(example_batches)

if __name__ == "__main__":
    main()
