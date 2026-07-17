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

@app.get('/expenses')
def send_expenses():
    return expenses

@app.post('/expenses')
def add_expense(expense: Expense):

    # Because we can also remove the expenses now, we can't simply use the length of the list for the id for the next element to be added. Instead, we could use the (id of the last element) + 1
    new_expense_id = expenses[-1]["id"] + 1

    new_expense = {
        "id": new_expense_id,
        **expense.dict()
    }

    expenses.append(new_expense)

    with open("./expenses.json", "w") as file:
        json.dump(expenses, file, indent = 4)

    
@app.delete('/expenses/{id}')
def remove_expense(id: int):

    global expenses

    new_expenses = [
        expense for expense in expenses
        if expense["id"] != id
    ]

    expenses = new_expenses

    with open("./expenses.json", "w") as file:
        json.dump(new_expenses, file, indent = 4)




    


