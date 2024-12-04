# Naprogramuj funkci, která určí známku studenta na základě průměru:
# A: 90 and above
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
#
# input:
# {
#   "Alice": [85, 90, 78],
# }
#
# output:
# {
#   "Alice": "B",
# }




def student_grades(students: dict[str,list[int]]) -> dict[str,str]:
    return {student: 
                "A" if sum(grades) / len(grades) >= 90 else
                "B" if sum(grades) / len(grades) >= 80 else
                "C" if sum(grades) / len(grades) >= 70 else
                "D" if sum(grades) / len(grades) >= 60 else
                "F"
        for student, grades in students.items()
    }




assert student_grades({"Alice": [85, 90, 78]}) == {
    "Alice": "B"
}, "Test case 1 failed"

assert student_grades({"Bob": [95, 92, 88]}) == {
    "Bob": "A"
}, "Test case 2 failed"

assert student_grades({"Charlie": [70, 75, 72]}) == {
    "Charlie": "C"
}, "Test case 3 failed"

assert student_grades({"David": [60, 65, 62]}) == {
    "David": "D"
}, "Test case 4 failed"

assert student_grades({"Eve": [50, -55, -58]}) == {
    "Eve": "F"
}, "Test case 5 failed"
