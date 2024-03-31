from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

students = []

class StudentName(Resource):
    def get(self, name):
        print(students)

        for stud in students:
            if stud['name'] == name:
                return stud
        return {'student': None}, 404
    
    def post(self, name):
        stud = {'name': name}
        students.append(stud)
        return stud, 201
    
    def delete(self, name):
        for ind,stud in enumerate(students):
            if stud['name'] == name:
                deleted_stud=students.pop(ind)
                return {'message': 'Item deleted'}
            class AllNames(Resource):
                def get(self):
                    return {'students': students}
                
            api.add_resource(StudentName, '/student/<string:name>')
            api.add_resource(AllNames, '/students')

if __name__ == '__main__':
    app.run(debug=True)