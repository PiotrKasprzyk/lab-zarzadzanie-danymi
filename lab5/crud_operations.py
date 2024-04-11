from basicmodel import app, db, Student

app.app_context().push()


print(f'\n***** **** **** (0) check of initial db')
all_students = Student.query.all()
print(f'all_students: {all_students}')


print(f'\n***** **** **** (1) create new student')
new_student = Student('Piotr', 6)
db.session.add(new_student)
db.session.commit()

all_students = Student.query.all()
print(f'all_students: {all_students}')

print(f'\n read')
all_students = Student.query.all()
print(f'all_students: {all_students}')

print(f'\nselect by id')
student_first = db.session.get(Student, 1)
print(f'student_first: {student_first.name}')
print(f'student_first: {student_first}')
all_students = Student.query.all()
print(f'all_students: {all_students}')

print(f'\n filtres')
student_piotr = Student.query.filter_by(name='Piotr')
print(f'student_piotr: {student_piotr}')
print(f'\n check')
print(f'Student (Piotr):\n{student_piotr.all()}')
print(f'update')
first_student = student_piotr.first()
first_student.name='Natalia'
first_student.semestr=7
db.session.add(first_student)
db.session.commit()
all_students = Student.query.all()  
print(f'all_students: {all_students}')

print(f'\n delete')
second_student = db.session.get(Student, 2)
db.session.delete(second_student)
db.session.commit()

all_students = Student.query.all()
print(f'all_students: {all_students}')

