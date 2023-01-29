from flask import request, jsonify, abort
from app import app
from app.models import app as p2p_app

@app.route("/users", methods=["POST"])
def add_user():
  data = request.get_json()
  new_user_name = data.get('name', None)
  new_user_email = data.get('email', None)

  if new_user_name is None or new_user_email is None:
      abort(400)
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
  user_id = data.get('userId', None)
  amount = data.get('amount', None)
  
  if user_id is None or amount is None:
    abort(400)
  
  foundUser = p2p_app.get_user(user_id)
  if foundUser is None:
    return jsonify({"success": False, "error": "user not found"}), 404

  try:
    user = p2p_app.deposit(user_id, amount)
    return jsonify({
      "success": True,
      "user": {"name": user.name, "balance": user.balance}
    })
  except:
    abort(422)

@app.route("/withdraw", methods=["POST"])
def withdraw():
  data = request.get_json()
  name = data["name"]
  amount = data["amount"]
  user = p2p_app.withdraw(name, amount)
  return jsonify({"name": user.name, "balance": user.balance})

@app.route("/send_money", methods=["POST"])
def send_money():
  data = request.get_json()
  sender = data["sender"]
  receiver = data["receiver"]
  amount = data["amount"]
  sender_user, receiver_user = p2p_app.send_money(sender, receiver, amount)
  return jsonify({"sender": sender_user.name, "receiver": receiver_user.name})

# ERROR HANDLERS
@app.errorhandler(404)
def not_found(error):
  return (
      jsonify({"success": False, "error": 404, "message": "Resource Not Found"}),
      404
  )

@app.errorhandler(422)
def unprocessable(error):
  return (jsonify({"success": False, "error": 422, "message": "unprocessable"}), 422)

@app.errorhandler(400)
def bad_request(error):
  return (jsonify({"success": False, "error": 400, "message": "bad request"}), 400)

@app.errorhandler(500)
def bad_request(error):
  return (jsonify({"success": False, "error": 500, "message": "Internal server error"}), 500)
