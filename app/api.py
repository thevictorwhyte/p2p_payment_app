from flask import request, jsonify, abort
from app import app
from app.models import app as p2p_app
from errors.validate_request_data import validate_request_data

@app.route("/users", methods=["POST"])
def add_user():
  data = request.get_json()
  error = validate_request_data(data, ['name', 'email'])

  if error:
    return jsonify({"error": error}), 400

  new_user_name = data.get('name', None)
  new_user_email = data.get('email', None)

  try:
    user = p2p_app.add_user(new_user_name, new_user_email)
    return jsonify({
      "success": True,
      "user": {"id": user.userId, "name": user.name, "email": user.email, "balance": user.balance}
    })
  except:
      abort(422)


@app.route("/deposit", methods=["POST"])
def deposit():
  data = request.get_json()
  error = validate_request_data(data, ['email', 'amount'])

  if error:
    return jsonify({"error": error}), 400

  email = data.get('email', None)
  amount = data.get('amount', None)
  
  foundUser = p2p_app.get_user(email)
  if foundUser is None:
    return jsonify({"success": False, "error": "user not found"}), 404

  try:
    user = p2p_app.deposit(email, amount)
    return jsonify({
      "success": True,
      "user": {"name": user.name, "email": user.email, "balance": user.balance}
    })
  except:
    abort(422)

@app.route("/withdraw", methods=["POST"])
def withdraw():
  data = request.get_json()
  error = validate_request_data(data, ['email', 'amount'])

  if error:
    return jsonify({"error": error}), 400

  email = data.get('email', None)
  amount = data.get('amount', None)

  foundUser = p2p_app.get_user(email)
  if foundUser is None:
    return jsonify({"success": False, "error": "user not found"}), 404

  try:
    user = p2p_app.withdraw(email, amount)
    return jsonify({
      "success": True,
      "user": {"name": user.name, "email": user.email, "balance": user.balance}
    })
  except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route("/send_money", methods=["POST"])
def send_money():
  data = request.get_json()
  error = validate_request_data(data, ['senderEmail', 'receiverEmail', 'amount'])

  if error:
    return jsonify({"sucess": False, "error": error}), 400

  sender_email = data.get('senderEmail', None)
  sender = p2p_app.get_user(sender_email)
  if sender is None: 
    return jsonify({"success": False, "error": "sender not found"}), 404
  receiver_email = data.get('receiverEmail', None)
  receiver = p2p_app.get_user(receiver_email)
  if receiver is None: 
    return jsonify({"success": False, "error": "receiver not found"}), 404
  amount = data.get('amount', None)

  try:
    sender_user, receiver_user = p2p_app.send_money(sender_email, receiver_email, amount)
    return jsonify({
      "success": True,
      "data": {"sender": sender_user.name, "receiver": receiver_user.name, "amount": amount}
    })
  except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400
  
@app.route("/balance", methods=["POST"])
def check_balance():
  data = request.get_json()
  error = validate_request_data(data, ['email'])
  if error:
    return jsonify({'success': False, "error": error}), 400

  try:
    email = data.get('email', None)
    user = p2p_app.get_user(email)

    if user is None:
      return jsonify({ "success": False, "error": "No user exists with that email"}), 404

    balance = p2p_app.check_balance(user.email)
    return jsonify({
      "success": True,
      "user": {
        "name": user.name,
        "balance": balance
      }
    })
  except:
    abort(422)

  

# ERROR HANDLERS
@app.errorhandler(404)
def not_found(error):
  return (
      jsonify({"success": False, "error": 404, "message": "Resource Not Found"}),
      404
  )

@app.errorhandler(422)
def unprocessable(error):
  return (jsonify({"success": False, "error": 422, "message": "The request was well-formed but was unable to be followed due to semantic errors"}), 422)

@app.errorhandler(400)
def bad_request(error):
  return (jsonify({"success": False, "error": 400, "message": "bad request"}), 400)

@app.errorhandler(500)
def bad_request(error):
  return (jsonify({"success": False, "error": 500, "message": "An internal error has occurred"}), 500)
