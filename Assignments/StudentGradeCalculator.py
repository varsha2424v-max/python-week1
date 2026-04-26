def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
    

def main():
    n = int(input("Enter number of subjects: "))
    marks = []

    for i in range(n):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    avg = calculate_average(marks)
    grade = assign_grade(avg)

    print("\n--- Result ---")
    print("Average Marks =", avg)
    print("Grade =", grade)


main()