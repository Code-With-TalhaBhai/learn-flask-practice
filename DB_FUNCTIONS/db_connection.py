import psycopg2


DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/postgres'

def connectToDb():
    return psycopg2.connect(DATABASE_URI)