# from flask import Flask, render_template, request, redirect, g
# import sqlite3

# app = Flask(__name__)
# DATABASE = "data.db"
# app.config["DATABASE"] = DATABASE


# def get_db():
#     db = getattr(g, "_database", None)
#     if db is None:
#         db = g._database = sqlite3.connect(app.config["DATABASE"])
#     return db


# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, "_database", None)
#     if db is not None:
#         db.close()


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/add", methods=["POST"])
# def add_record():
#     # Get database connection
#     db = get_db()
#     cursor = db.cursor()

#     bk_name = request.form["bk_name"]
#     bk_id = request.form["bk_id"]
#     author_name = request.form["author_name"]
#     bk_status = request.form["bk_status"]

#     if bk_status == "Issued":
#         card_id = issuer_card()
#     else:
#         card_id = "N/A"

#     try:
#         cursor.execute(
#             "INSERT INTO Library (BK_NAME, BK_ID, AUTHOR_NAME, BK_STATUS, CARD_ID) VALUES (?, ?, ?, ?, ?)",
#             (bk_name, bk_id, author_name, bk_status, card_id),
#         )
#         db.commit()

#         return redirect("/view")
#     except sqlite3.IntegrityError:
#         return "Book ID already in use!"


# @app.route("/view")
# def view_records():
#     # Get database connection
#     db = get_db()
#     cursor = db.cursor()

#     cursor.execute("SELECT * FROM Library")
#     records = cursor.fetchall()

#     return render_template("view.html", records=records)


# @app.route("/update", methods=["POST"])
# def update_record():
#     # Get database connection
#     db = get_db()
#     cursor = db.cursor()

#     bk_id = request.form["bk_id"]
#     bk_name = request.form["bk_name"]
#     author_name = request.form["author_name"]
#     bk_status = request.form["bk_status"]

#     if bk_status == "Issued":
#         card_id = issuer_card()
#     else:
#         card_id = "N/A"

#     cursor.execute(
#         "UPDATE Library SET BK_NAME=?, BK_STATUS=?, AUTHOR_NAME=?, CARD_ID=? WHERE BK_ID=?",
#         (bk_name, bk_status, author_name, card_id, bk_id),
#     )
#     db.commit()

#     return redirect("/view")


# @app.route("/delete/<string:bk_id>")
# def delete_record(bk_id):
#     # Get database connection
#     db = get_db()
#     cursor = db.cursor()

#     cursor.execute("DELETE FROM Library WHERE BK_ID=?", (bk_id,))
#     db.commit()

#     return redirect("/view")


# def issuer_card():
#     Cid = request.args.get("issuer_id")

#     if not Cid:
#         return "N/A"
#     else:
#         return Cid


# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, g
# import sqlite3

# app = Flask(__name__)
# DATABASE = "data.db"
# app.config["DATABASE"] = DATABASE


# def get_db():
#     db = getattr(g, "_database", None)
#     if db is None:
#         db = g._database = sqlite3.connect(app.config["DATABASE"])
#     return db


# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, "_database", None)
#     if db is not None:
#         db.close()


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/add", methods=["POST"])
# def add_record():
#     # Get database connection
#     db = get_db()
#     cursor = db.cursor()

#     bk_name = request.form["bk_name"]
#     bk_id = request.form["bk_id"]
#     author_name = request.form["author_name"]
#     bk_status = request.form["bk_status"]

#     if bk_status == "Issued":
#         card_id = issuer_card()
#     else:
#         card_id = "N/A"

#     try:
#         cursor.execute(
#             "INSERT INTO Library (BK_NAME, BK_ID, AUTHOR_NAME, BK_STATUS, CARD_ID) VALUES (?, ?, ?, ?, ?)",
#             (bk_name, bk_id, author_name, bk_status, card_id),
#         )
#         db.commit()

#         return redirect("/view")
#     except sqlite3.IntegrityError:
#         return "Book ID already in use!"


# @app.route("/view")
# def view_records():
#     # Get database connection
#     db = get_db()
#     cursor = db.cursor()

#     cursor.execute("SELECT * FROM Library")
#     records = cursor.fetchall()

#     return render_template("view.html", records=records)


# @app.route("/update/<string:bk_id>", methods=["GET", "POST"])
# def update_record(bk_id):
#     # Get database connection
#     db = get_db()
#     cursor = db.cursor()

#     if request.method == "POST":
#         bk_name = request.form["bk_name"]
#         author_name = request.form["author_name"]
#         bk_status = request.form["bk_status"]

#         if bk_status == "Issued":
#             card_id = issuer_card()
#         else:
#             card_id = "N/A"

#         cursor.execute(
#             "UPDATE Library SET BK_NAME=?, BK_STATUS=?, AUTHOR_NAME=?, CARD_ID=? WHERE BK_ID=?",
#             (bk_name, bk_status, author_name, card_id, bk_id),
#         )
#         db.commit()

#         return redirect("/view")

#     # Fetch the record to pre-populate the form
#     cursor.execute("SELECT * FROM Library WHERE BK_ID=?", (bk_id,))
#     record = cursor.fetchone()

#     return render_template("update.html", record=record)


# @app.route("/delete/<string:bk_id>")
# def delete_record(bk_id):
#     # Get database connection
#     db = get_db()
#     cursor = db.cursor()

#     cursor.execute("DELETE FROM Library WHERE BK_ID=?", (bk_id,))
#     db.commit()

#     return redirect("/view")


# def issuer_card():
#     Cid = request.args.get("issuer_id")

#     if not Cid:
#         return "N/A"
#     else:
#         return Cid


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, g
import sqlite3

app = Flask(__name__)
DATABASE = "data.db"
app.config["DATABASE"] = DATABASE


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(app.config["DATABASE"])
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_record():
    # Get database connection
    db = get_db()
    cursor = db.cursor()

    bk_name = request.form["bk_name"]
    bk_id = request.form["bk_id"]
    author_name = request.form["author_name"]
    bk_status = request.form["bk_status"]

    if bk_status == "Issued":
        card_id = issuer_card(request.form.get("issuer_id"))
    else:
        card_id = "N/A"

    try:
        cursor.execute(
            "INSERT INTO Library (BK_NAME, BK_ID, AUTHOR_NAME, BK_STATUS, CARD_ID) VALUES (?, ?, ?, ?, ?)",
            (bk_name, bk_id, author_name, bk_status, card_id),
        )
        db.commit()

        return redirect("/view")
    except sqlite3.IntegrityError:
        return "Book ID already in use!"


@app.route("/view")
def view_records():
    # Get database connection
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Library")
    records = cursor.fetchall()

    return render_template("view.html", records=records)


@app.route("/update/<string:bk_id>", methods=["GET", "POST"])
def update_record(bk_id):
    # Get database connection
    db = get_db()
    cursor = db.cursor()

    if request.method == "POST":
        bk_name = request.form["bk_name"]
        author_name = request.form["author_name"]
        bk_status = request.form["bk_status"]

        if bk_status == "Issued":
            card_id = issuer_card(request.form.get("issuer_id"))
        else:
            card_id = "N/A"

        cursor.execute(
            "UPDATE Library SET BK_NAME=?, BK_STATUS=?, AUTHOR_NAME=?, CARD_ID=? WHERE BK_ID=?",
            (bk_name, bk_status, author_name, card_id, bk_id),
        )
        db.commit()

        return redirect("/view")

    # Fetch the record to pre-populate the form
    cursor.execute("SELECT * FROM Library WHERE BK_ID=?", (bk_id,))
    record = cursor.fetchone()

    return render_template("update.html", record=record)


@app.route("/delete/<string:bk_id>")
def delete_record(bk_id):
    # Get database connection
    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM Library WHERE BK_ID=?", (bk_id,))
    db.commit()

    return redirect("/view")


def issuer_card(issuer_id):
    if issuer_id:
        return issuer_id
    else:
        return "N/A"


if __name__ == "__main__":
    app.run(debug=True)
