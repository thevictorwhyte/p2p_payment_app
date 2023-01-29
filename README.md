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
Documentation of available API endpoints including the URL, request parameters, and the response body.

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

### `POST /deposit`
- Deposit money into the system.
- Sample Request body:
  ```json
  {
    "email": "victor@gmail.com",
    "amount": 10
  }
  ```
- Sample response object:
  ```json
  {
    "success": true,
    "user": {
        "balance": 10,
        "email": "victor@gmail.com",
        "name": "Victor David"
    }
  }
  ```

### `POST /withdraw`
- Transfer money out of the system.
- Sample Request body:  
  ```json
  {
    "email": "victor@gmail.com",
    "amount": 10
  }
  ```
- Sample response object:
  ```json
  {
    "success": true,
    "user": {
        "balance": 10,
        "email": "victor@gmail.com",
        "name": "Victor David"
    }
  }
  ```

### `POST /send_money`
- Send money to other app users.
- Sample Request body:  
  ```json
  {
    "senderEmail": "victor@gmail.com",
    "receiverEmail": "david@gmail.com",
    "amount": 25
  }
  ```
- Sample response object:
  ```json
  {
    "data": {
        "amount": 25,
        "receiver": "David Mark",
        "sender": "Victor David"
    },
    "success": true
  }
  ```

### `POST /balance`
- Check balance.
- Sample Request body:  
  ```json
  {
    "email": "david@gmail.com"
  }
  ```
- Sample response object:
  ```json
  {
    "success": true,
    "user": {
        "balance": 30,
        "name": "David Mark"
    }
  }
  ```


