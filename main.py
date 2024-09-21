from flask import Flask, render_template

from data import db


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", title="Моя супер піцерія")


@app.get("/menu-ababagalamaga/")
def menu():
    pizzas_db = db.get_pizzas()
    pizzas = []
    for pizza in pizzas_db:
        pizzas.append(
            {"name": pizza[1], "ingredients": pizza[2], "price": pizza[3]}
        )

    context = {
        "pizzas": pizzas,
        "title": "Мега меню"
    }
    return render_template("menu.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
