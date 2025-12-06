from fastapi import FastAPI
from database import engine
import databaseModels

app = FastAPI(title="My Product")

# Create DB tables
databaseModels.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "Hello, Welcome to our application"}
