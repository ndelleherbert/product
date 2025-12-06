from fastapi import FastAPI
from database import engine
import databaseModels

# Create DB tables
databaseModels.Base.metadata.create_all(bind=engine)

app = FastAPI(title="My Product")


@app.get("/")
def greet():
    return {"message": "Hello, Welcome to our application"}
