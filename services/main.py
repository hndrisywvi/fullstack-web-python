from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import app as service
import datastore
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.debug = True

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    res, err = service.login(username, password)
    if err:
        flash(f"Login failed: {err}")
    elif res:
        flash("Login successful")
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid username or password")
    return redirect(url_for('index'))

@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    username = request.form["reg_username"]
    password = request.form["reg_password"]
    role = request.form["role"]
    timestamp = request.form["timestamp"]

    existing_user, _ = datastore.get_user_by_username(username)
    if existing_user:
        flash("Username already exists. Please choose a different username.")
        return redirect(url_for('index'))

    success, error = service.register(name, username, password, role)
    if error:
        flash(f"Registration failed: {error}")
    else:
        flash("Registration successful")
    return redirect(url_for('index'))

@app.route("/dashboard")
def dashboard():
    # keyword = request.form["keyword"]
    # page = request.form["page"]
    # limit = request.form["limit"]
    
    res, err = service.getListUserAccount(None, 1, 1)
    if err != None:
        print(err)
    
    if res in (None, []):
        msg = flash("data not found")
        return render_template("dashboard.html", msg = msg)
    
    return render_template('dashboard.html', data=res)

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    success, error = service.delete(id)
    if error:
        flash(f"Delete error: {error}")
    else:
        flash("Data successfully deleted")
    return redirect(url_for('dashboard'))

@app.route("/update_username", methods=["POST"])
def update_username():
    id = request.form.get("id")
    new_username = request.form.get("new_username")
    success, error = service.update_username(id, new_username)
    if error:
        flash(f"Update username error: {error}")
    else:
        flash("Username updated successfully")
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run()
