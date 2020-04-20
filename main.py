from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from myform import LoginForm
from flask_bootstrap import Bootstrap



app=Flask(__name__)
Bootstrap(app)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///index.db'
app.config['SECRET_KEY']='secret_key'

db=SQLAlchemy(app)

class Member(db.Model):

    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    random = db.Column(db.String(20))

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('index.html',form=form)

if __name__=='__main__':
    app.run(debug=True)