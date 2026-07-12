import csv
import os

FILE_NAME = "students.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "student_id",
                "name",
                "mathematics",
                "programming",
                "networking",
                "database",
                "average",
                "status"
            ])


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    mathematics = float(input("Mathematics mark: "))
    programming = float(input("Programming mark: "))
    networking = float(input("Networking mark: "))
    database = float(input("Database mark: "))

    average = (
        mathematics +
        programming +
        networking +
        database
    ) / 4

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            student_id,
            name,
            mathematics,
            programming,
            networking,
            database,
            round(average, 2),
            status
        ])

    print("\nStudent added successfully.\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n----- STUDENT RECORDS -----")

            for row in reader:
                print(" | ".join(row))

            print()

    except FileNotFoundError:
        print("No student records found.")


def search_student():
    search_id = input("Enter student ID: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == search_id:
                print("\nStudent found:")
                print(" | ".join(row))
                found = True
                break

    if not found:
        print("Student not found.")


def generate_report():
    total_students = 0
    passed = 0
    failed = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_students += 1

            if row["status"] == "Pass":
                passed += 1
            else:
                failed += 1

    print("\n----- REPORT -----")
    print(f"Total students: {total_students}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print()


def menu():

    create_file()

    while True:

        print("===== STUDENT PERFORMANCE DASHBOARD =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            generate_report()

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


menu()
