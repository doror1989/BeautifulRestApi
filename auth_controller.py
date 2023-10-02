from flask import Flask, request, jsonify
app = Flask(__name__)

class test:

    def is_authenticated(func):
        def wrapper(*args, **kwargs):
            return True

    def check_balanace():
        loan: int = 50
        logger.info(f"{loan}")
    
    @is_authenticated
    @app.route("/protected_route/:id")
    def protected_route(id):
        return jsonify({"message": f"Hello, {id}! This is a protected route."})

    
    @is_authenticated
    @app.route("/protected_route_2/:email")
    def protected_route_2(email):
        return jsonify({"message": f"Hello, {user.username}! This is a protected route."})


    @app.route("/not protected_route/")
    def not_protected_route(user,id):
        return jsonify({"message": f"Hello, {user.username}! This is not a protected route."})
