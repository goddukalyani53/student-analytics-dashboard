import sqlite3
from datetime import date, timedelta

DB_NAME = "college.db"

STUDENTS = [
    (1, "Aarav Sharma", "CSE"),
    (2, "Priya Patel", "ECE"),
    (3, "Rohan Mehta", "ME"),
    (4, "Ananya Reddy", "CSE"),
    (5, "Kabir Singh", "EEE"),
    (6, "Meera Iyer", "CSE"),
    (7, "Vikram Nair", "Civil"),
    (8, "Sneha Gupta", "ECE"),
    (9, "Aditya Rao", "IT"),
    (10, "Ishita Banerjee", "IT"),
]

RESOURCES = [
    (1, "Data Structures Notes", 142),
    (2, "Operating Systems Lab Manual", 87),
    (3, "Digital Electronics Question Bank", 63),
    (4, "Python for Data Analysis Cheatsheet", 210),
    (5, "Engineering Mathematics Formula Sheet", 175),
]


def build_attendance_rows():
    """Generate 10 weekdays of mixed present/absent records for each student."""
    start = date(2026, 8, 17)  # Monday
    weekday_offsets = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11]  # two academic weeks
    absences = {
        2: {date(2026, 8, 19)},
        3: {date(2026, 8, 18), date(2026, 8, 25)},
        5: {date(2026, 8, 21)},
        7: {date(2026, 8, 17), date(2026, 8, 26)},
        8: {date(2026, 8, 20)},
        10: {date(2026, 8, 24)},
    }

    rows = []
    record_id = 1
    for student_id, _, _ in STUDENTS:
        missed = absences.get(student_id, set())
        for offset in weekday_offsets:
            day = start + timedelta(days=offset)
            status = "Absent" if day in missed else "Present"
            rows.append((record_id, student_id, day.isoformat(), status))
            record_id += 1
    return rows


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.executescript(
        """
        DROP TABLE IF EXISTS attendance;
        DROP TABLE IF EXISTS resources;
        DROP TABLE IF EXISTS students;

        CREATE TABLE students (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            branch TEXT
        );

        CREATE TABLE attendance (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            date TEXT,
            status TEXT
        );

        CREATE TABLE resources (
            id INTEGER PRIMARY KEY,
            resource_name TEXT,
            downloads INTEGER
        );
        """
    )

    cursor.executemany(
        "INSERT INTO students (student_id, name, branch) VALUES (?, ?, ?)",
        STUDENTS,
    )
    cursor.executemany(
        "INSERT INTO attendance (id, student_id, date, status) VALUES (?, ?, ?, ?)",
        build_attendance_rows(),
    )
    cursor.executemany(
        "INSERT INTO resources (id, resource_name, downloads) VALUES (?, ?, ?)",
        RESOURCES,
    )

    conn.commit()
    conn.close()
    print(f"Created {DB_NAME} with students, attendance, and resources.")


if __name__ == "__main__":
    create_database()
