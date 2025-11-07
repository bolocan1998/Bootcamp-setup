import psycopg2

try:
    conn = psycopg2.connect(
        dbname="dvdrental",   # sau DB-ul tău
        user="postgres",
        password="marcelbolocan98",
        host="127.0.0.1",     # important: IPv4
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    print("✅ Connected:", cur.fetchone()[0])
except Exception as e:
    print("❌ Connection failed:", e)
finally:
    if 'cur' in locals(): cur.close()
    if 'conn' in locals(): conn.close()

