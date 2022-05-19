from ensurepip import version
import psycopg2

con = None

try:
    con = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost", port="5432")

    cur = con.cursor()
    cur.execute("SELECT version()")

    version = cur.fetchone()[0]
    print("ok")
    print(version)

except psycopg2.DatabaseError as e:
    print(f"Error {e}")

finally:

    if con:
        cur.close()
        con.close()

