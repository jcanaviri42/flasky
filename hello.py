from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)


@app.get("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return f"<p>Your browser is {user_agent}</p>"


@app.get("/user/<name>")
def user(name):
    if name not in ["Dave", "Mary", "John"]:
        abort(404)

    return f"<h1>Hello, {name}!</h1>"


@app.get("/carries-cookie")
def carries_cookie():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie("answer", "42")

    return response


@app.get("/redirect-me")
def redirect_me():
    return redirect("http://www.example.com")


@app.post("/user")
def create_user():
    json_body = request.get_json()
    return f"Creating a user with the name: {json_body.get('name')}"
