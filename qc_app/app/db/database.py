import sqlite3

DB_PATH = "sqlite.db"


def init_db() -> None:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analytes (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            level TEXT NOT NULL,
            unit TEXT NOT NULL,
            mean REAL NOT NULL,
            standard_deviation REAL NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY,
            analyte_id INTEGER NOT NULL,
            result_value REAL NOT NULL,
            z_score REAL NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('PASS', 'WARNING', 'FAIL')),
            violation TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (analyte_id) REFERENCES analytes(id)
        )
        """
    )

    connection.commit()
    connection.close()