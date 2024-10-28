#Q1:

#Task: You are given a dictionary of student names and scores. Write a Python program that takes this dictionary as an argument and returns the name of the student with the highest score.
#Example:
#Given student_scores = { "Alice": 92, "Bob": 78, "Charlie": 85, "David": 98, "Eve": 91 }
#Expected Output:
"The student with the highest score is David."


def highest_score(student_scores):
    # Find the key (student) with the highest value (score) using max() function
    top_student = max(student_scores, key=student_scores.get)
    return f"The student with the highest score is {top_student}"

# Example dictionary
student_scores = { "Alice": 92, "Bob": 78, "Charlie": 85, "David": 98, "Eve": 91 }

# Calling the function
print(highest_score(student_scores))
