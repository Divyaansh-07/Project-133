from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route("/")
def home():
    name="Harry Potter"
    age="18"
    return render_template('index.html',name=name,age=age)
@app.route("/father")
def father():
    name="James Potter"
    age="25"
    return render_template('father.html',name=name,age=age)
@app.route("/mother")
def mother():
    name="Lily Potter"
    age="24"
    return render_template('mother.html',name=name,age=age)
@app.route("/friends")
def friends():
    name="Ron and Hermione"
    age="18"
    return render_template('friends.html',name=name,age=age)
app.run(debug=True)