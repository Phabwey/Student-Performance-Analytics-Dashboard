import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt

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

    student_id = entry_id.get()
    name = entry_name.get()

    try:

        mathematics = float(entry_math.get())
        programming = float(entry_programming.get())
        networking = float(entry_networking.get())
        database = float(entry_database.get())

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid marks."
        )

        return

    if (
        mathematics < 0 or mathematics > 100 or
        programming < 0 or programming > 100 or
        networking < 0 or networking > 100 or
        database < 0 or database > 100
    ):

        messagebox.showerror(
            "Error",
            "Marks must be between 0 and 100."
        )

        return

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if row[0] == student_id:

                messagebox.showerror(
                    "Error",
                    "Student ID already exists."
                )

                return

    average = (
        mathematics +
        programming +
        networking +
        database
    ) / 4

    status = "Pass" if average >= 50 else "Fail"

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

    messagebox.showinfo(
        "Success",
        "Student added successfully."
    )

    clear_fields()


def clear_fields():

    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_math.delete(0, tk.END)
    entry_programming.delete(0, tk.END)
    entry_networking.delete(0, tk.END)
    entry_database.delete(0, tk.END)


def view_students():

    text_output.delete(1.0, tk.END)

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            text_output.insert(
                tk.END,
                " | ".join(row) + "\n"
            )


def generate_report():

    total_students = 0
    passed = 0
    failed = 0

    highest_average = 0
    top_student = ""

    total_average = 0

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

    report = (
        f"Total students: {total_students}\n"
        f"Passed: {passed}\n"
        f"Failed: {failed}\n"
        f"Class average: {class_average:.2f}%\n"
        f"Top student: {top_student} "
        f"({highest_average:.2f}%)"
    )

    messagebox.showinfo(
        "Class Report",
        report
    )


def generate_chart():

    passed = 0
    failed = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["status"] == "Pass":
                passed += 1
            else:
                failed += 1

    labels = ["Pass", "Fail"]
    values = [passed, failed]

    plt.figure(figsize=(6, 6))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title(
        "Student Performance Summary"
    )

    plt.show()


def show_top_performer():

    highest_average = 0
    top_student = ""

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            average = float(row["average"])

            if average > highest_average:

                highest_average = average
                top_student = row["name"]

    messagebox.showinfo(
        "Top Performer",
        f"{top_student}\nAverage: {highest_average:.2f}%"
    )


def class_summary():

    total_students = 0
    total_average = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            total_students += 1
            total_average += float(row["average"])

    if total_students > 0:

        class_average = total_average / total_students

    else:

        class_average = 0

    messagebox.showinfo(
        "Class Summary",
        f"Students: {total_students}\n"
        f"Class Average: {class_average:.2f}%"
    )


create_file()

root = tk.Tk()

root.title(
    "Student Performance Dashboard"
)

root.geometry(
    "800x750"
)

title = tk.Label(
    root,
    text="Student Performance Dashboard",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

tk.Label(
    root,
    text="Student ID"
).pack()

entry_id = tk.Entry(
    root,
    width=40
)

entry_id.pack()

tk.Label(
    root,
    text="Student Name"
).pack()

entry_name = tk.Entry(
    root,
    width=40
)

entry_name.pack()

tk.Label(
    root,
    text="Mathematics"
).pack()

entry_math = tk.Entry(
    root,
    width=40
)

entry_math.pack()

tk.Label(
    root,
    text="Programming"
).pack()

entry_programming = tk.Entry(
    root,
    width=40
)

entry_programming.pack()

tk.Label(
    root,
    text="Networking"
).pack()

entry_networking = tk.Entry(
    root,
    width=40
)

entry_networking.pack()

tk.Label(
    root,
    text="Database"
).pack()

entry_database = tk.Entry(
    root,
    width=40
)

entry_database.pack()

tk.Button(
    root,
    text="Add Student",
    command=add_student
).pack(pady=5)

tk.Button(
    root,
    text="View Students",
    command=view_students
).pack(pady=5)

tk.Button(
    root,
    text="Generate Report",
    command=generate_report
).pack(pady=5)

tk.Button(
    root,
    text="Generate Chart",
    command=generate_chart
).pack(pady=5)

tk.Button(
    root,
    text="Top Performer",
    command=show_top_performer
).pack(pady=5)

tk.Button(
    root,
    text="Class Summary",
    command=class_summary
).pack(pady=5)

text_output = tk.Text(
    root,
    height=15,
    width=90
)

text_output.pack(pady=10)

root.mainloop()
