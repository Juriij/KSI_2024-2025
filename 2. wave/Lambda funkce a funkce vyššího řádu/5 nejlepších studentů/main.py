student_lst = [
    {"name": "Karlík", "scores": [90, 85, 92]},
    {"name": "Los Karlos", "scores": [15, 75, 66]},
    {"name": "Sob Karsob", "scores": [50, 55, 60]},
    {"name": "Losa Manuelosa", "scores": [0, 4, 100]},
    {"name": "Sova Karsova", "scores": [99, 95, 98]},
    {"name": "Lemur Lofard", "scores": [65, 60, 70]},
    {"name": "Tux", "scores": [85, 10, 91]}
]

# Tuto funkci implementuj.
def top_5(students, criteria_func):
    top_students_final = []

    sorted_students = sorted(students, key=lambda student: criteria_func(student["scores"]), reverse=True)

    if len(sorted_students) <= 5:
        top_students = sorted_students
    
    top_students = sorted_students[:5]
    
    top_students = sorted(top_students, key=lambda student: student["name"])

    for student in top_students:
        top_students_final.append(student["name"])

    
    return top_students_final




# Testy:
avg = lambda lst: sum(lst) / len(lst) if lst else 0
print(top_5(student_lst, avg))  # ['Karlík', 'Lemur Lofard', 'Sob Karsob', 'Sova Karsova', 'Tux']
print(top_5(student_lst, max))  # ['Karlík', 'Los Karlos', 'Losa Manuelosa', 'Sova Karsova', 'Tux']
