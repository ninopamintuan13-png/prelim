# ============================================
# Student Grade Management System
# Name: Niño Pamintuan | Year: 2nd Year IT
# ============================================

def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 75:
        return "C"
    elif grade >= 50:
        return "D"
    else:
        return "F"


def check_pass_or_fail(grade):
    if grade >= 75:
        return "PASSED"
    else:
        return "FAILED"


def save_student_record(first_name, last_name, grade, letter_grade, status):
    with open("grade.txt", "a") as file:
        file.write(f"{first_name} {last_name} | {grade} | {letter_grade} | {status}\n")


def main():  # Niño Pamintuan | 2nd Year IT
    while True:
        print("\n--- Enter Student Info ---")
        
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        
        try:
            grade = float(input("Grade (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        letter_grade = get_letter_grade(grade)
        status = check_pass_or_fail(grade)

        print("\n--- Result ---")
        print(f"Name: {first_name} {last_name}")
        print(f"Grade: {grade}")
        print(f"Letter Grade: {letter_grade}")
        print(f"Status: {status}")

        save_student_record(first_name, last_name, grade, letter_grade, status)
        print("Saved to file successfully!")

        choice = input("\nAdd another student? (yes/no): ").lower()
        if choice != "yes":
            print("Program ended.")
            break


if __name__ == "__main__":
    main()