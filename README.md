# P2P Payment App Backend

## Prerequisites
- Python 3.x
- Flask


## Development Setup
1. Clone the repository
`git clone https://github.com/thevictorwhyte/p2p-payment-app.git`

2. Navigate to the project directory
`cd p2p-payment-app`

3. Create a virtual environment
`python3 -m venv venv`

4. Activate the virtual environment
`source venv/bin/activate`

5. Install the required package(s)
`pip install -r requirements.txt`


## Usage
1. Start the Flask development server
`python run.py`

2. The backend should now be running at `http://localhost:5000/`.

## File Structure

```
.
├── app
│   ├── __init__.py
│   ├── api.py
│   └── models.py
├── tests
│   └── test_api.py
├── venv
├── requirements.txt
├── run.py
└── README.md
```

## Endpoints Documentation
Documentation of available API endpoints including the URL, request parameters, and the response body
- `/users` (POST)
  - POST: Add a new user
- `/deposit` (POST)
  - POST: Deposit money into the app
- `/transfer` (POST)
  - POST: Send money to another user in the app
- `/balance` (POST)
  - POST: Retrieve a user's balance in the app
- `/withdraw` (POST)
  - POST: Transfer money out of the app

### `POST /users`
- Adds a new user to the system.
- Sample Request body:
  ```json
  {
    "name": "Victor Whyte",
    "email": "victor@gmail.com"
  }
  ```
- Sample response object:
  ```json
  {
    "success": true,
    "user": {
        "balance": 0,
        "email": "victor@gmail.com",
        "id": "8edfe67e-2a8d-428e-bcf5-0fc9aa8db63c",
        "name": "Victor David"
    }
  }
  ```


