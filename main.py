
import csv
import os

FILE_NAME = "students.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "student_id","name","mathematics","programming",
                "networking","database","average","status"
            ])


def add_student():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            for row in csv.DictReader(file):
                if row["student_id"].lower() == student_id.lower():
                    print("\nStudent ID already exists.\n")
                    return

    try:
        mathematics = float(input("Mathematics mark: "))
        programming = float(input("Programming mark: "))
        networking = float(input("Networking mark: "))
        database = float(input("Database mark: "))
    except ValueError:
        print("\nPlease enter valid numbers.\n")
        return

    marks = [mathematics, programming, networking, database]
    if any(m < 0 or m > 100 for m in marks):
        print("\nMarks must be between 0 and 100.\n")
        return

    average = round(sum(marks) / 4, 2)
    status = "Pass" if average >= 50 else "Fail"

    with open(FILE_NAME, "a", newline="") as file:
        csv.writer(file).writerow([
            student_id, name, mathematics, programming,
            networking, database, average, status
        ])

    print("\nStudent added successfully.\n")


def view_students():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            found = False
            print("\n" + "=" * 60)
            print("STUDENT RECORDS")
            print("=" * 60)
            for row in reader:
                found = True
                print(f"Student ID   : {row['student_id']}")
                print(f"Name         : {row['name']}")
                print(f"Mathematics  : {row['mathematics']}")
                print(f"Programming  : {row['programming']}")
                print(f"Networking   : {row['networking']}")
                print(f"Database     : {row['database']}")
                print(f"Average      : {row['average']}%")
                print(f"Status       : {row['status']}")
                print("-" * 60)
            if not found:
                print("No student records found.")
    except FileNotFoundError:
        print("No student records found.")


def search_student():
    search = input("Enter student ID or name: ").strip().lower()
    found = False
    try:
        with open(FILE_NAME, "r", newline="") as file:
            for row in csv.DictReader(file):
                if row["student_id"].lower() == search or row["name"].lower() == search:
                    found = True
                    print("\n" + "=" * 50)
                    print("STUDENT FOUND")
                    print("=" * 50)
                    for k in ["student_id","name","mathematics","programming","networking","database","average","status"]:
                        print(f"{k.replace('_',' ').title():13}: {row[k]}")
                    print("=" * 50)
        if not found:
            print("Student not found.")
    except FileNotFoundError:
        print("No student records found.")


def display_top_student():
    top = None
    try:
        with open(FILE_NAME, "r", newline="") as file:
            for row in csv.DictReader(file):
                if top is None or float(row["average"]) > float(top["average"]):
                    top = row
        if not top:
            print("No student records available.")
            return
        print("\n" + "=" * 50)
        print("TOP PERFORMING STUDENT")
        print("=" * 50)
        for k in ["student_id","name","mathematics","programming","networking","database","average","status"]:
            print(f"{k.replace('_',' ').title():13}: {top[k]}")
        print("=" * 50)
    except FileNotFoundError:
        print("No student records found.")


def generate_report():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            rows = list(csv.DictReader(file))
        if not rows:
            print("No student records available.")
            return
        total = len(rows)
        passed = sum(r["status"] == "Pass" for r in rows)
        failed = total - passed
        class_avg = sum(float(r["average"]) for r in rows) / total
        top = max(rows, key=lambda r: float(r["average"]))
        pass_rate = (passed / total) * 100
        print("\n----- CLASS REPORT -----")
        print(f"Total Students : {total}")
        print(f"Passed         : {passed}")
        print(f"Failed         : {failed}")
        print(f"Pass Rate      : {pass_rate:.2f}%")
        print(f"Class Average  : {class_avg:.2f}%")
        print(f"Top Student    : {top['name']} ({float(top['average']):.2f}%)")
    except FileNotFoundError:
        print("No student records found.")


def menu():
    create_file()
    print("=" * 60)
    print("STUDENT PERFORMANCE ANALYTICS DASHBOARD")
    print("=" * 60)
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Generate Report")
        print("5. Display Top Performing Student")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            display_top_student()
        elif choice == "6":
            print("\nThank you for using the Student Performance Dashboard.")
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    menu()
