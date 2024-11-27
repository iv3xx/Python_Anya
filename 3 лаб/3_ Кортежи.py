from collections import namedtuple

SubjectGrades = namedtuple('SubjectGrades', ['subject', 'grade'])

grades = [
    SubjectGrades('Math', 95),
    SubjectGrades('Physics', 85),
    SubjectGrades('Chemistry', 90),
    SubjectGrades('Biology', 88),
    SubjectGrades('Literature', 92)
]

# Вычисляем средний балл
def calculate_average(grades):
    total = sum(grade.grade for grade in grades)  
    average = total / len(grades)  
    return average

average_grade = calculate_average(grades)

print("Оценки:")
for grade in grades:
    print(f"{grade.subject}: {grade.grade}")

print("Средний балл:", average_grade)
