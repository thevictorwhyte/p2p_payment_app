# P2P Payment App Backend

## Prerequisites
- Python 3.x
- Flask

## Installation
1. Clone the repository
`git clone https://github.com/[your_username]/p2p-payment-app-backend.git`

2. Navigate to the project directory
`cd p2p-payment-app-backend`

3. Create a virtual environment
`python3 -m venv venv`

4. Activate the virtual environment
`source venv/bin/activate`

5. Install the required package(s)
`pip install -r requirements.txt`


## Usage
1. Start the Flask development server
`python run.py`

2. The backend should now be running at `http://localhost:5000/`. To verify, navigate to `http://localhost:5000/users` in your browser or using a tool such as `curl` or `httpie`. You should receive a message saying "Welcome to the P2P Payment App Backend".

## Endpoints
- `/users` (GET and POST)
  - GET: Retrieve details of a user
  - POST: Add a new user
- `/deposit` (POST)
  - POST: Deposit money into the app
- `/transfer` (POST)
  - POST: Send money to another user in the app
- `/balance` (GET)
  - GET: Retrieve a user's balance in the app
- `/withdraw` (POST)
  - POST: Transfer money out of the app


