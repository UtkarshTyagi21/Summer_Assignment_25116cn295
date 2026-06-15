#WAP to move zeroes to end.
def move_zeros_to_end(students):
    insert_pos = 0 #Index to place the next non-zero element forward

    for student in students: #Step 1: Move all non-zero elements forward
        if student != 0:
            students[insert_pos] = student
            insert_pos += 1

    while insert_pos < len(students) :
        students[insert_pos] = 0
        insert_pos += 1
    return students

#Example usage:
#Let's say 0 represents a student who dropped out or an empty seat
student_list = [101,0,103,0,105,106,0,108]

print("Original list: ", student_list)
sorted_students = move_zeros_to_end(student_list)
print("Modified list: ", sorted_students)