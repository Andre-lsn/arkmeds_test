import psycopg2
import os

DATABASE = os.getenv("DATABASE")
USER_DATABASE = os.getenv("USER_DATABASE")
HOST="localhost"
PORT="5432"

conn = psycopg2.connect(f"dbname={DATABASE} user={USER_DATABASE} host={HOST} port={PORT}")
cursor = conn.cursor()

# def create_call_table():
#   cursor.execute("""
#     CREATE TABLE IF NOT EXISTS call(
#       id SERIAL PRIMARY KEY,
#       called,
#       priority_color,
#       priority,
#       not_urgent,
#       number,
#       requester,
#       service_equipment,
#       criticality,
#       time,
#       closing time,
#       responsible_str,
#       technical resp,
#       problem_str,
#       called_id,
#       call_field,
#       state,
#       inserted_at timestamp DEFAULT current_timestamp,
#       updated_at timestamp DEFAULT current_timestamp
#     )
#   """)
#   conn.commit()

def create_equipament_table():
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipament(
      id SERIAL PRIMARY KEY,
      equipament_id INTEGER,
      manufacturer VARCHAR(100),
      patrimonio VARCHAR(100),
      serial_number VARCHAR(10),
      inserted_at timestamp DEFAULT current_timestamp,
      updated_at timestamp DEFAULT current_timestamp
    );
  """)
  conn.commit()


def create_detailed_company_table():
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS detailed_company(
      id SERIAL PRIMARY KEY,
      type INTEGER,
      name VARCHAR(255),
      fantasy_name VARCHAR(255),
      higher INTEGER,
      cnpj VARCHAR(20),
      cep VARCHAR(255),
      comments VARCHAR(100),
      contact VARCHAR(20),
      email VARCHAR(255),
      phone1 VARCHAR(20),
      phone2 VARCHAR(20),
      extension1 VARCHAR(255),
      extension2 VARCHAR(255),
      fax VARCHAR(255),
      street VARCHAR(255),
      number INTEGER,
      complement VARCHAR(255),
      neighborhood VARCHAR(255),
      city VARCHAR(255),
      state VARCHAR(255),
      inserted_at timestamp DEFAULT current_timestamp,
      updated_at timestamp DEFAULT current_timestamp
    );
  """)
  conn.commit()

def save_detailed_company_data(type, name, fantasy_name, higher, cnpj, cep, comments, contact, email, phone1, phone2, extension1, extension2, fax, street, number, complement, neighborhood, city, state):
  fields = (
    type,
    name,
    fantasy_name,
    higher,
    cnpj,
    cep,
    comments,
    contact,
    email,
    phone1,
    phone2,
    extension1,
    extension2,
    fax,
    street,
    number,
    complement,
    neighborhood,
    city,
    state
  )

  cursor.execute("""
    INSERT INTO detailed_company (type, name, fantasy_name, higher, cnpj, cep, comments, contact, email, phone1, phone2, extension1, extension2, fax, street, number, complement, neighborhood, city, state)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """,
    fields
  )
  conn.commit()
