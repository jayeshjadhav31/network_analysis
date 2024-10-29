import psycopg2

def connection():
    # Define your connection parameters
    db_config = {
        'dbname': 'iit_bombay',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost',  # or your database host
        'port': '5432'        # default PostgreSQL port
    }

    # Connect to the database
    try:
        connection = psycopg2.connect(**db_config)
        print("Connection successful!")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    
    return connection

