import sqlite3

DATABASE = "data/metrics.db"


def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpu REAL,
            memory REAL,
            disk REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_metrics(cpu, memory, disk):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO metrics (cpu, memory, disk)
        VALUES (?, ?, ?)
    """, (cpu, memory, disk))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM metrics
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows