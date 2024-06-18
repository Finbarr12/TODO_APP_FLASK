from flask import Blueprint,request,flash,redirect,url_for,render_template
from model.model import User
from _init_ import db

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/")
def welcome():
    return "Wecome to the todo app"

@user_bp.route("/signup", methods =['GET','POST'])
def signupUser():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmPass = request.form.get("confirmPass")

        if not name or not email or not password:
            flash("Error! All fields are required.","error")

        elif  password != confirmPass:
            flash("Password must be Confirm password","warning")    
        else:
            try:
                new_user = User(name=name,email=email,password=password)
                db.session.add(new_user)
                db.session.commit()
                flash("Sucess You have signed Up", 'success')
                return redirect(url_for("user_bp.signupUser"))
            except ValueError as e:
                flash(str(e),"error")
    return render_template("signup.html")        
