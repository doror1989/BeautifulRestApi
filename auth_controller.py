from flask import Flask, request, jsonify
app = Flask(__name__)

class test:

    def is_authenticated(func):
        def wrapper(*args, **kwargs):
            return True

    @app.route("/protected_route/")
    @is_authenticated
    def protected_route(user,id):
        return jsonify({"message": f"Hello, {user.username}! This is a protected route."})


    @app.route("/not protected_route/")
    def not_protected_route(user,id):
        return jsonify({"message": f"Hello, {user.username}! This is not a protected route."})
