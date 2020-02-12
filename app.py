from flask import Flask, render_template # render template allows us to 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #this creates an app with the name being given the name of our file
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://michelle:Mobet-11@localhost:5432/todoapp'
db = SQLAlchemy(app) #this db object links SQL alchemy to our flask app

class Todo(db.Model):
	__tablename__ = 'todos'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(), nullable=False)

def __repr__(self):
	return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/') #sets up a route to listen to our homepage
def index():
	return render_template('index.html', data=Todo.query.all()
		)