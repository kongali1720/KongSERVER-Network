# backup_database.py
# Backup otomatis untuk KongSERVER database

import os
import datetime
import subprocess

# Konfigurasi (bisa pakai .env untuk keamanan)
DB_TYPE = "mysql"  # "mysql" atau "postgres"
DB_NAME = "kongserver_db"
DB_USER = "root"
DB_PASS = "passwordku"
BACKUP_DIR = "/backup/kongserver/"

# Pastikan folder backup ada
os.makedirs(BACKUP_DIR, exist_ok=True)

# Nama file backup
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = f"{BACKUP_DIR}{DB_NAME}_{timestamp}.sql"

# Jalankan perintah backup
try:
    if DB_TYPE == "mysql":
        cmd = f"mysqldump -u {DB_USER} -p{DB_PASS} {DB_NAME} > {backup_file}"
    elif DB_TYPE == "postgres":
        cmd = f"PGPASSWORD={DB_PASS} pg_dump -U {DB_USER} {DB_NAME} > {backup_file}"
    else:
        raise ValueError("DB_TYPE tidak dikenali!")

    subprocess.run(cmd, shell=True, check=True)
    print(f"[✔] Backup sukses: {backup_file}")
except Exception as e:
    print("[✘] Gagal backup:", e)
