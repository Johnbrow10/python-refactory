from flask import Flask, render_template, flash
from datetime import datetime
from filtros import format_date

app = Flask(__name__,
template_folder="views",
static_folder="public")

app.config["SECRET_KEY"] = "secret"
app.jinja_env.filters["formatdate"] = format_date

@app.route("/templates")
def templates():
    
    user_page = True
    
    return render_template("index.html", user_page=user_page)


@app.route("/usuarios")
def users():
    users =  [{
        "name": "johnatan",
        "idade": 75,
        "email": "john@gmail.com" ,
        "active": True,
        "since": datetime.utcnow()
    },
    {
        "name": "gustavo",
        "idade": 10,
        "email": "gustavo@gmail.com" ,
        "active": False,
        "since": datetime.utcnow()
    }]
    
    flash(message="User routes",category="success")
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)