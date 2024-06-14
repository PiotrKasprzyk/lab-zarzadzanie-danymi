from fastapi import FastAPI
from db.database import engine
from db import models
from router import user

app = FastAPI()
app.include_router(user.router)

@app.get('/')
def index():
    return {
        'message': 'The example of using a FastAPI within the SQLite database'
    }
    
models.Base.metadata.create_all(engine)