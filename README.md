# Expense Tracker Backend

Backend API for the Expense Tracker app built during Day 3 of the Locus Software Fellowship program at Pulchowk Campus.

This repository contains only the backend service. It is designed to work with a frontend that can be hosted separately on another platform, while still communicating with this API through CORS-enabled requests.

## What this project does

- Serves expense data through a small FastAPI application.
- Stores data in a local `expenses.json` file.
- Supports cross-origin requests so a separate frontend can call the API.
- Does not serve frontend static assets from this repository.

## Prerequisites

Before you start, make sure you have:

- Python 3.11 or newer
- `pip` available from the terminal

Verify your Python installation:

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

## Getting Started

### 1. Clone the repository, or download the zip file

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

### 2. Create a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
```

Windows:

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows Command Prompt:

```bash
.venv\Scripts\activate
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

After activation, you should see `(.venv)` at the start of your terminal prompt.

### 4. Install the project dependencies

```bash
pip install -r requirements.txt
```

If `pip` is not available, use:

```bash
python -m pip install -r requirements.txt
```

### 5. Start the FastAPI development server

```bash
uvicorn app.main:app --reload
```

You should see output similar to:

```bash
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 6. Open the API in your browser

Visit:

- http://127.0.0.1:8000

FastAPI also exposes interactive documentation:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## API Overview

The backend currently provides a small expenses API.

### Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/expenses` | Returns the full list of expenses |
| `POST` | `/expenses` | Adds a new expense |
| `DELETE` | `/expenses/{id}` | Deletes an expense by ID |

### Expense shape

The API accepts and stores expenses in this format:

```json
{
  "name": "Coffee",
  "amount": 7
}
```

The stored records include an auto-generated `id`:

```json
{
  "id": 11,
  "name": "Coffee",
  "amount": 7
}
```

### Example requests

Get all expenses:

```bash
curl http://127.0.0.1:8000/expenses
```

Create a new expense:

```bash
curl -X POST http://127.0.0.1:8000/expenses \
  -H "Content-Type: application/json" \
  -d '{"name":"Lunch","amount":15}'
```

Delete an expense:

```bash
curl -X DELETE http://127.0.0.1:8000/expenses/3
```

## Frontend and CORS

This backend is intentionally API-only. It does not bundle or serve the frontend static files, which makes it easier to deploy the frontend and backend on separate platforms.

The app is configured with CORS middleware so browser-based frontend apps can make requests to it. In the current development setup, all origins are allowed. That is convenient for local development, but for production you should restrict `allow_origins` to the actual frontend domain.

Example deployment setup:

- Frontend hosted on one platform
- Backend hosted on another platform
- Frontend sends API requests to the backend URL
- CORS allows those cross-origin browser requests

## Data Storage

Expense data is stored in the local `expenses.json` file.

Important notes:

- Restarting the server keeps the data only if `expenses.json` is preserved.
- The app writes directly to the JSON file when you add or delete expenses.
- This is simple and great for learning, but not a substitute for a database in production.

## Project Structure

```text
expense-tracker-backend/
├── app/
│   └── main.py
├── expenses.json
├── requirements.txt
└── README.md
```

## Example Seed Data

The repository ships with sample expenses such as:

- Groceries
- Rent
- Electricity Bill
- Internet
- Gas

These records are useful for testing the API immediately after startup.

## Troubleshooting

- If `uvicorn` is not found, make sure the virtual environment is activated and dependencies are installed.
- If Python points to an older version, try `python3` instead of `python`.
- If browser requests fail from the frontend, check the backend CORS settings and verify the frontend is calling the correct API URL.

## Notes for Contributors

- Keep the API surface small and easy to understand.
- If you add a real database later, update this README and the setup steps.
- If you change the frontend deployment story, update the CORS section to match.
