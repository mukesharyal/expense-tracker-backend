# Import the various objects from the FastAPI library
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the json standard library
import json

# Import the BaseModel class for JSON support
from pydantic import BaseModel

# This class Expense will tell us the structure in which the POST request data will be accepted
class Expense(BaseModel):
    name: str
    amount: int

# Open the file in read mode, and store the contents in the variable expenses
with open("./expenses.json", "r") as file:
    expenses = json.load(file)

# Create an instance of the FastAPI app
app = FastAPI()

# Allow cross origin requests to the server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

    


