"""
5.  The Head of Computing at the University of Poppleton is tasked with dividing a
    group of students into lab groups. A lab group is 24 students, since this is the
    number of PCs in a lab. Write a program that calculates how many groups are
    needed for the following number of students: 113, 175, 12. Display how many full
    groups there will be, and how many students will be in the smaller "left over"
    group.
"""

# Define the maximum number of students per group
students_per_group = 24

# Calculate groups and leftover students for Group A
group_a_students = 113
group_a_complete = group_a_students // students_per_group  # Number of complete groups
group_a_leftover = group_a_students % students_per_group   # Leftover students

# Calculate groups and leftover students for Group B
group_b_students = 175
group_b_complete = group_b_students // students_per_group
group_b_leftover = group_b_students % students_per_group

# Calculate groups and leftover students for Group C
group_c_students = 120
group_c_complete = group_c_students // students_per_group
group_c_leftover = group_c_students % students_per_group

# Calculate total groups and leftover students
total_groups = group_a_complete + group_b_complete + group_c_complete
total_leftovers = group_a_leftover + group_b_leftover + group_c_leftover

print("There will be a total of", total_groups, "complete groups.")
print("There will be", total_leftovers, "students left over.")
