import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="admin0695",
    host="localhost",
    port="5432",
    dbname="oilparts_db"
)

print("✅ Успешное подключение!")
conn.close()
