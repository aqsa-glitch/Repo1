import os
FILE_NAME = "students.txt"

def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "Fail"
    return avg, grade



def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll No: ")
    marks = []
    for i in range(1, 4):
        mark = int(input(f"Enter Marks of Subject {i}: "))
        marks.append(mark)

    avg, grade = calculate_grade(marks)

    record = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "average": avg,
        "grade": grade
    }

    with open(FILE_NAME, "a") as f:
        f.write(str(record) + "\n")

    print("\n Student record added successfully!")



def view_students():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found!")
        return

    with open(FILE_NAME, "r") as f:
        students = f.readlines()

    if not students:
        print(" No records found!")
        return

    print("\n===== All Students =====")
    for line in students:
        student = eval(line.strip())
        print(f"Name: {student['name']}, Roll: {student['roll']}, "
              f"Marks: {student['marks']}, Average: {student['average']:.2f}, Grade: {student['grade']}")



def search_student():
    roll_no = input("Enter Roll No to search: ")
    found = False

    if not os.path.exists(FILE_NAME):
        print("⚠️ No records found!")
        return

    with open(FILE_NAME, "r") as f:
        for line in f:
            student = eval(line.strip())
            if student['roll'] == roll_no:
                print("\n===== Student Found =====")
                print(f"Name: {student['name']}, Roll: {student['roll']}, "
                      f"Marks: {student['marks']}, Average: {student['average']:.2f}, Grade: {student['grade']}")
                found = True
                break

    if not found:
        print(" Student not found!")



def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print(" Exiting program...")
            break
        else:
            print(" Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
