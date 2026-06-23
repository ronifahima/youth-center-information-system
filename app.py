import os
from flask import Flask, render_template, request, redirect, session, flash
from response import Response
from db_connection import get_db_connection

# -------------------------------------------------
# נתיב בסיס
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------------------------------
# Flask config
# -------------------------------------------------
app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_url_path="/static"
)

app.secret_key = "secret_key_for_course"

# -------------------------------------------------
# Login
# -------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT * FROM users
            WHERE username = %s AND password = %s
        """, (username, password))

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:
            session["user_id"] = user["id"]
            session["first_name"] = user["first_name"]
            session["last_name"] = user["last_name"]
            session["phone"] = user["phone"]
            session["username"] = user["username"]

            return redirect("/profile")

        return render_template("login.html", error="שם משתמש או סיסמה שגויים")

    return render_template("login.html")


# -------------------------------------------------
# אזור אישי
# -------------------------------------------------
@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect("/")
    return render_template("profile.html")


# -------------------------------------------------
# פתיחת פנייה
# -------------------------------------------------
@app.route("/open_request", methods=["GET", "POST"])
def open_request():
    if "user_id" not in session:
        return redirect("/")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":
        subject = request.form["subject"]
        description = request.form["description"]

        cursor.execute("""
            INSERT INTO requests (user_id, subject, description, status)
            VALUES (%s, %s, %s, %s)
        """, (session["user_id"], subject, description, "פתוחה"))

        connection.commit()
        cursor.close()
        connection.close()

        flash("הפנייה נשלחה בהצלחה", "success")
        return redirect("/open_request")

    cursor.close()
    connection.close()
    return render_template("open_request.html")


# -------------------------------------------------
# הפניות שלי + סינון + תגובות
# -------------------------------------------------
@app.route("/my_requests")
def my_requests():
    if "user_id" not in session:
        return redirect("/")

    selected_status = request.args.get("status")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if selected_status and selected_status != "הכל":
        cursor.execute("""
            SELECT requests_id, subject, description, status, opened_at, closed_at
            FROM requests
            WHERE user_id = %s AND status = %s
            ORDER BY opened_at DESC
        """, (session["user_id"], selected_status))
    else:
        cursor.execute("""
            SELECT requests_id, subject, description, status, opened_at, closed_at
            FROM requests
            WHERE user_id = %s
            ORDER BY opened_at DESC
        """, (session["user_id"],))

    requests_list = cursor.fetchall()

    # 🔧 כאן התיקון החשוב – שליפת response_date
    for req in requests_list:
        cursor.execute("""
            SELECT content, response_date
            FROM responses
            WHERE request_id = %s
            ORDER BY response_date ASC
        """, (req["requests_id"],))
        req["responses"] = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "my_requests.html",
        requests=requests_list,
        selected_status=selected_status or "הכל"
    )


# -------------------------------------------------
# שליחת תגובה לפנייה
# -------------------------------------------------
@app.route("/response", methods=["POST"])
def add_response():
    if "user_id" not in session:
        return redirect("/")

    response = Response(
        request_id=request.form["request_id"],
        content=request.form["content"],
        sender="צעיר"
    )

    # response_date מתמלא אוטומטית ע"י MySQL
    response.send_response()
    return redirect("/my_requests")


# -------------------------------------------------
# סגירת פנייה
# -------------------------------------------------
@app.route("/close_request", methods=["POST"])
def close_request():
    if "user_id" not in session:
        return redirect("/")

    request_id = request.form["request_id"]

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT status
        FROM requests
        WHERE requests_id = %s AND user_id = %s
    """, (request_id, session["user_id"]))

    req = cursor.fetchone()

    if req and req["status"] != "סגורה":
        cursor.execute("""
            UPDATE requests
            SET status = %s,
                closed_at = NOW()
            WHERE requests_id = %s
        """, ("סגורה", request_id))
        connection.commit()

    cursor.close()
    connection.close()

    return redirect("/my_requests")


# -------------------------------------------------
# Logout
# -------------------------------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# -------------------------------------------------
# Run
# -------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
