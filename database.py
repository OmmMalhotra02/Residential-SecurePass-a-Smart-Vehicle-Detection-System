import sqlite3
db_file = "vehicle_data.db"
conn = sqlite3.connect("vehicle_data.db")

curs = conn.cursor()
#sqlite3.connect("vehicle_databse.db")
#db_file=open('vehicle_database.db')
#cursor = conn.cursor()

license_plates = [
    "MH48BE9641",
    "MH12DE1433",
    "BB44K4446",
    "UP14DV8828",
    "AP29AJ9099",
    "MH12FK0512",
    "AP23R1651",
    "KL18W3485",
    "AP28BV9276",
    "MH03BE6763",
    "KL14S8439",
    "KLO7CJ8999",
    "AP11AE3196",
    "TN33AJ7490",
    "TN22CF4740",
    "MH04EF3337",
    "MH12FV5288",
    "DL2CAL7538",
    "MH42GV4495",
    "DL3SBS9880"
]

def create_tables(conn, cursor):
  """
  Creates tables if they don't exist.
  """
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS residents (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      license_plate TEXT,
      driver_name INTEGER
    );
  """)

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS driver_faces (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      resident_id INTEGER REFERENCES residents(id),
      face_image BLOB
    );
  """)

residents = []
for i in range(20):
  name = f"Resident_{i+1}" 
  residents.append({"name": name})

driversName = []
for i in range(20):
  dname = f"Driver_{i+1}"
  driversName.append(dname)

def insert_residents(residents, license_plates, driversName, db_file="vehicle_data.db"):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    for i, resident in enumerate(residents):
        name = resident["name"]
        dname = driversName[i]
        license_plate = license_plates[i] if i < len(license_plates) else None
        cursor.execute("INSERT INTO residents (name, license_plate, driver_name) VALUES (?, ?, ?)", (name, license_plate, dname))

    conn.commit()
    conn.close()

create_tables(conn, curs)
print("Resident data saved to database!")

def connect_to_database():
  """
  Connects to the database and returns a connection and cursor object.
  """
  conn = sqlite3.connect("vehicle_data.db")
  cursor = conn.cursor()
  return conn, cursor

def close_connection(conn):
  """
  Commits changes and closes the database connection.
  """
  conn.commit()
  conn.close()

def print_residents(cursor):
  """
  Prints resident data from the database.
  """
  cursor.execute("SELECT * FROM residents")
  residents = cursor.fetchall()

  if not residents:
    print("No residents found in the database!")
    return

  print("Residents:")
  print(residents)
  for resident in residents:
    # Access data by column index or name
    _,resident_id, name, license_plate = resident
    dname = resident
    print(f"ID: {resident_id}, Name: {name}, License Plate: {license_plate}, Driver Name: {dname}")