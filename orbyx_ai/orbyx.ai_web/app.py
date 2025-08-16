from flask import Flask, render_template, request, redirect, url_for
from chatbot import get_response

app = Flask(__name__)

chat_history = []

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/chat", methods=["GET", "POST"])
def index():
    global chat_history
    user_input = ""
    bot_response = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_response(user_input)
        chat_history.append(("You", user_input))
        chat_history.append(("Orbyx AI", bot_response))

    return render_template("index.html", chat_history=chat_history)

@app.route("/reset")
def reset():
    global chat_history
    chat_history = []
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
