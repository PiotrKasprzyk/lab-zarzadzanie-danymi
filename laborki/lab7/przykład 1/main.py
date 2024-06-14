from fastapi import FastAPI

app = FastAPI()

EMPLOYEES = [
    {'firstname': 'Łukasz', 'lastname': 'Piątek'},
    {'firstname': 'Piotr', 'lastname': 'Nowak'}
]

@app.get('/')
async def index_api():
    return {
        'message': 'The example of a simple use of FastAPI'
    }
    
@app.get('/employees')
async def get_employees():
    return EMPLOYEES

@app.get('/employee/{name}')
async def get_one_employee(name: str):
    for emp in EMPLOYEES:
        if emp['lastname'] == name:
            return emp
    return {
        'employee': f'Employee with lastname {name} was not found'
    }, 404