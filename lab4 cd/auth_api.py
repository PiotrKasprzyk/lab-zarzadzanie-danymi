from flask import Flask, request
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
api = Api(app)

jwt = JWT(app, authenticate, identity)

students = []

class StudentNames(Resource):
    def get(self, name):
        print(students)

        for stud in students:
            if stud['name'] == name: 
                return stud

        return {'name': None}, 404

    def post(self, name):
        stud = {'name': name}
        students.append(stud)
        print(students)
        return stud

    def delete(self, name):
        for ind, stud in enumerate(students):
            if stud['name'] == name:
                deleted_stud = students.pop(ind)
                return {'note': ' delete successful'}

class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {"students": students}

api.add_resource(StudentNames, '/student/<string:name>')
api.add_resource(AllNames, '/students')

if __name__ == '__main__':
    app.run(debug=True)