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

    try:
        mathematics = float(input("Mathematics mark: "))
        programming = float(input("Programming mark: "))
        networking = float(input("Networking mark: "))
        database = float(input("Database mark: "))

    except ValueError:
        print("\nPlease enter valid numbers.\n")
        return

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

    search = input(
        "Enter student ID or name: "
    ).lower()

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if (
                row[0].lower() == search or
                row[1].lower() == search
            ):

                print("\nStudent found:")
                print(" | ".join(row))
                found = True

    if not found:
        print("Student not found.")

def display_top_student():

    highest_average = -1
    top_student = None

    try:
        with open(FILE_NAME, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                average = float(row["average"])

                if average > highest_average:
                    highest_average = average
                    top_student = row

        if top_student is None:
            print("\nNo student records available.\n")
            return

        print("\n" + "=" * 50)
        print("🏆 TOP PERFORMING STUDENT")
        print("=" * 50)
        print(f"Student ID   : {top_student['student_id']}")
        print(f"Name         : {top_student['name']}")
        print(f"Mathematics  : {top_student['mathematics']}")
        print(f"Programming  : {top_student['programming']}")
        print(f"Networking   : {top_student['networking']}")
        print(f"Database     : {top_student['database']}")
        print(f"Average      : {top_student['average']}%")
        print(f"Status       : {top_student['status']}")
        print("=" * 50)

    except FileNotFoundError:
        print("\nNo student records found.\n")

def generate_report():

    total_students = 0
    passed = 0
    failed = 0
    total_average = 0

    top_student = ""
    highest_average = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            average = float(row["average"])

            total_students += 1
            total_average += average

            if row["status"] == "Pass":
                passed += 1
            else:
                failed += 1

            if average > highest_average:
                highest_average = average
                top_student = row["name"]

    if total_students > 0:
        class_average = total_average / total_students
    else:
        class_average = 0

    print("\n----- CLASS REPORT -----")
    print(f"Total students: {total_students}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(
        f"Class average: {class_average:.2f}%"
    )
    print(
        f"Top student: {top_student} ({highest_average:.2f}%)"
    )
    print()

def menu():

    create_file()

    while True:

        print("\n===== STUDENT PERFORMANCE DASHBOARD =====")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Generate Report")
        print("5. Display Top Performing Student")
        print("6. Exit")

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

            display_top_student()

        elif choice == "6":

    print("\nThank you for using the Student Performance Dashboard.")
    print("Goodbye!\n")
    break

        else:

            print("\nInvalid option. Please try again.\n")


if __name__ == "__main__":
    menu()


