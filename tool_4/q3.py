# 3.Write a Python function student_data () 
# which will print the id of a student (student_id). 
# If the user passes an argument student_name or student_class the 
# function will print the student name and class.

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name:{kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name:{kwargs['student_name']}")
            print(f"Student Class:{kwargs['student_class']}")

 
student_data(student_id='1928024', student_name='Bishop')

student_data(student_id='19280000', student_name='kip', student_class ='CSSE')