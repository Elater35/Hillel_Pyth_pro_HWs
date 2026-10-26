from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_name = request.form.get("name")
        favorite_genre = request.form.get("genre")
        return redirect(f"/books?name={user_name}&genre={favorite_genre}")
    return render_template("index.html")

@app.route("/books", methods=["GET", "POST"])
def books():
    user_name = request.args.get("name")
    favorite_genre = request.args.get("genre")
    return render_template("books.html", name=user_name, genre=favorite_genre)

app.run(debug=True)
