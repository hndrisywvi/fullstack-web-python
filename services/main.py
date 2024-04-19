from flask import Flask, render_template, request, flash, redirect, url_for
import app as service

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
    confirm_password = request.form["confirm_password"]

    if password != confirm_password:
        flash("Passwords do not match")
        return redirect(url_for('index'))

    success, error = service.register(name, username, password)
    if error:
        flash(f"Registration failed: {error}")
    else:
        flash("Registration successful")
    return redirect(url_for('index'))

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()
