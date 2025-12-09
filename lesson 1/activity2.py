import numpy as np

data_types = [("name", "S15"), ("class", int)]

student_details = [
    ("Ali", 8),
    ("Aysha", 5),
    ("Fatima", 2)
]

students = np.array(student_details, data_types)
sorted_array = np.sort(students, order="class")

print("Sorted Array:")
print(sorted_array)