from model import db, User, Products, Orders, OrderItem
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, url_for, redirect, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E_commerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATTIONS'] = False
app.config['SECRET_KEY'] = "super-secret"

jwt = JWTManager(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# register
@app.route("/", methods=['GET','POST'])
def Register():
    if request.method =="POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash("Username already exists", "danger")
            return render_template("register.html")
        if User.query.filter_by(email=email).first():
            flash("Email already exists", "danger")
            return render_template("register.html")
        hashed_password = generate_password_hash(password)
        user =User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! please login", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return render_template("index.html")
        flash("Invalid username or password", "danger")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(port=5009, debug=True)
