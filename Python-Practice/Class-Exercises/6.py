def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'name' in kwargs:
        print(f"Student's Name: {kwargs['student_name']}")
    
    if 'name' and 'class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")

 
student_data(student_id= '1234', name = 'Lebron James')

student_data(student_id='4321', name= 'John Doeing 737', Class= 'Super Rich')
# Why ask for it this way!? Because