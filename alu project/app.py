from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("alumni.db")
    return conn


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    year = request.form["year"]
    department = request.form["department"]

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO alumni (name,email,year,department) VALUES (?,?,?,?)",
        (name,email,year,department)
    )

    conn.commit()
    conn.close()

    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alumni")
    data = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", alumni=data)


app.run(debug=True)