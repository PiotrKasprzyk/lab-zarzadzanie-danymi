from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

students = []

class Student(Resource):
    def get(self, name):
        for student in students:
            if student['name'] == name:
                return student
        return {'student': None}, 404

    def post(self, name):
        student = {'name': name}
        students.append(student)
        return student, 201

    def delete(self, name):
        global students
        students = [student for student in students if student['name'] != name]
        return {'message': 'Item deleted'}
    
class Allnames(Resource):
    def get(self):
         return {'students': students}
        
api.add_resource(Student, '/student/<string:name>')
api.add_resource(Allnames, '/students')

if __name__ == '__main__':
    app.run(debug=True)