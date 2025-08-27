#  main.py -> Project entry point

import data
import utils

#  Add some students
data.add_student("Abdullateef", "AI Engineering")
data.add_student("Fopefoluwa", "AI Development")

# Print formatted student records
for s in data.get_students():
    print(utils.format_student(s))