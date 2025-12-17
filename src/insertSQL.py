import os
import psycopg2
from pathlib import Path

DB_HOST = os.getenv("DB_HOST_LOCAL", "localhost")
DB_NAME = os.getenv("DB_NAME_LOCAL")
DB_USER = os.getenv("DB_USER_LOCAL")
DB_PASSWORD = os.getenv("DB_PASSWORD_LOCAL")
DB_PORT = os.getenv("DB_PORT_LOCAL", "5432")

if not all([DB_NAME, DB_USER, DB_PASSWORD]):
    raise RuntimeError("variáveis de banco não definidas")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SQL_DIR = Path("/app/src/sql")

print(">>> conectando no banco:", DATABASE_URL)

conn = psycopg2.connect(DATABASE_URL)
conn.autocommit = False
cur = conn.cursor()

files = sorted(SQL_DIR.glob("*.sql"))

if not files:
    print("nenhum arquivo .sql encontrado")
    exit(0)

for sql_file in files:
    print(f">>> executando {sql_file.name}")
    with open(sql_file, "r", encoding="utf-8") as f:
        sql = f.read()

    try:
        cur.execute(sql)
        conn.commit()
        print(f"<<< {sql_file.name} OK")
    except Exception as e:
        conn.rollback()
        print(f"xxx erro em {sql_file.name}")
        print(e)
        break

cur.close()
conn.close()
print(">>> seeds finalizados")
