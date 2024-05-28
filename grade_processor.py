import csv

def read_csv(file_name):
    students = {}
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                name, grade = row[0], row[1]
                try:
                    grade = float(grade)
                except ValueError:
                    print(f"Warning: Grade for {name} is not a valid number. Skipping entry.")
                    continue
            students[name] = grade
    return students

def calculate_grades(students):
    grades = []
    for grade in students.values():
        grades.append(grade)
    average_grade = round((sum(grades) / len(grades)), 1)    
    highest_grade = max(grades)
    lowest_grade = min(grades)

    highest_grade_names = []
    for x in students:
        if float(students[x]) == highest_grade:
            highest_grade_names.append(x)

    lowest_grade_names = []
    for x in students:
        if float(students[x]) == lowest_grade:
            lowest_grade_names.append(x)

    return average_grade, highest_grade, lowest_grade, highest_grade_names, lowest_grade_names

def main():
    file_name = 'classRecord.csv'
    students = read_csv(file_name)

    average_grade, highest_grade, lowest_grade, highest_grade_names, lowest_grade_names = calculate_grades(students)
    
    print(f"Number of student(s) in the class: {len(students)}\n")
    print(f"Average grade of the class: {average_grade}")
    print(f"Highest class score: {highest_grade}")
    print(f"Lowest class score: {lowest_grade}\n")
    print(f"Name of student(s) who earned the highest score:")
    for i in range(1, len(highest_grade_names)+1):
        print(f"{i}. {highest_grade_names[i-1]}")
    print()
    print(f"Name of student(s) who earned the lowest score:")
    for i in range(1, len(lowest_grade_names)+1):
        print(f"{i}. {lowest_grade_names[i-1]}")

if __name__ == '__main__':
    main()