# Student Grade Manager

students = {}


def add_student(name):
    if name in students:
        print("Student already exists.")
    else:
        students[name] = []
        print("Student added successfully.")


def add_score(name, score):
    if name not in students:
        print("Student not found.")
    else:
        students[name].append(score)
        print("Score added successfully.")


def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def display_students():
    if not students:
        print("No students available.")
        return

    for name, scores in students.items():
        average = calculate_average(scores)
        print(f"Name: {name}, Scores: {scores}, Average: {average:.2f}")


def main():
    while True:
        print("\nStudent Grade Manager")
        print("1. Add Student")
        print("2. Add Score")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            try:
                score = float(input("Enter score: "))
                add_score(name, score)
            except ValueError:
                print("Invalid score.")

        elif choice == "3":
            display_students()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
