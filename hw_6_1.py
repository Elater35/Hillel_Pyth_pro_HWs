from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Привіт! Тут ти знайдеш інформацію про нашу книгу."


@app.route("/search")
def search_page():
    return render_template("search.html")


@app.route("/result")
def result_page():
    volume = request.args.get("volume_number")
    return f"На жаль, том {volume} відсутній."


if __name__ == "__main__":
    app.run(debug=True)
