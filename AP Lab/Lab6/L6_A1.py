import sqlite3
from datetime import datetime

# Connect to the SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect('clinical_appointments.db')
cursor = conn.cursor()

# Create a table to store appointment details
cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY,
        patient_name TEXT,
        doctor_name TEXT,
        appointment_date TEXT,
        appointment_time TEXT
    )
''')

# Commit changes and close the connection
conn.commit()

def create_appointment():
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
    appointment_time = input("Enter appointment time (HH:MM AM/PM): ")

    cursor.execute('''
        INSERT INTO appointments (patient_name, doctor_name, appointment_date, appointment_time)
        VALUES (?, ?, ?, ?)
    ''', (patient_name, doctor_name, appointment_date, appointment_time))

    conn.commit()
    print("Appointment created successfully!")

def view_appointments():
    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()

    if not appointments:
        print("No appointments found.")
    else:
        print("Appointments:")
        for appointment in appointments:
            print(f"Appointment ID: {appointment[0]}")
            print(f"Patient Name: {appointment[1]}")
            print(f"Doctor Name: {appointment[2]}")
            print(f"Appointment Date: {appointment[3]}")
            print(f"Appointment Time: {appointment[4]}\n")

def main():
    while True:
        print("\nClinical Appointment Management System")
        print("1. Create Appointment")
        print("2. View Appointments")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
