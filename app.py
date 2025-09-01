import sqlite3
from flask import Flask, request, render_template
from stats import load_data, plot_bmi

app = Flask(__name__)

#connect database
def create_table():
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            bmi REAL
        )
    """)
    conn.commit()
    conn.close()

#save values to database
def save_user(age, bmi):
    conn = sqlite3.connect("bmi_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (age, bmi) VALUES (?, ?)", (age, bmi))
    conn.commit()
    conn.close()

#head function
@app.route("/", methods=["GET","POST"])
def input_user():
    if request.method == "POST":
        age = int(request.form["age"])
        height = int(request.form["height"]) / 100
        weight = int(request.form["weight"])


        bmi = round(weight / height**2, 2)


        if bmi < 18.5:
            category = "Underweight"
        elif bmi <= 25:
            category ="Healthy weight"
        elif bmi < 30:
            category = "Overweight"
        elif bmi < 35:
            category = "Class 1 Obesity"
        elif bmi < 40:
            category = "Class 2 Obesity"
        else:
            category = "Class 3 Obesity"



        save_user(age, bmi)

        return render_template("index.html", message=f"Your bmi is {bmi} - {category}.")

    return render_template("index.html")
#graf site
@app.route("/stats")
def stats_page():
    data = load_data()
    plot_bmi(data)

    return render_template("stats.html")

#table site
@app.route("/table")
def table_page():
    data = load_data()

    return render_template("table.html", data=data)

#main module
if __name__ == "__main__":
    create_table()
    app.run(debug=True)
