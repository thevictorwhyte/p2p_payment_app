# P2P Payment App Backend

## Prerequisites
- Python 3.x
- Flask

## Install Dependencies

## Installation
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

## Endpoints
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


