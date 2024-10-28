def pass_or_fail(grades_dict, passing_grade):
    passed_students = []  # List to store students who pass
    for student, grades in grades_dict.items():
        average_grade = sum(grades) / len(grades)  # Calculate average grade
        if average_grade >= passing_grade:  # Check if average is >= passing grade
            passed_students.append(student)  # Add student to the passed list
    return passed_students  # Return the list of passed students


# Sample data
grades_dict = {
    "Alice": [85, 90, 88],
    "Bob": [70, 75, 72],
    "Dane": [10, 25, 32],
    "Charlie": [92, 88, 95]
}
passing_grade = 40

# Sample function call and output
result = pass_or_fail(grades_dict, passing_grade)
print(result)  # Output: ['Alice', 'Bob', 'Charlie']
