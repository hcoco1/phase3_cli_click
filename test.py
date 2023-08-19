import os

# Construct the full path to the database
db_path = os.path.join(os.getcwd(), 'db', 'geodata.db')

# Check if the file exists
if os.path.exists(db_path):
    print(f"Database exists at: {db_path}")
else:
    print(f"Database does not exist at: {db_path}")
