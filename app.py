from flask import Flask, render_template, request, redirect, url_for, jsonify
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


@app.route('/todos/create', methods=['POST'])
def create_todo():
	description = request.get_json()['description'] #uses get_json instead
	todo = Todo(description=description)
	db.session.add(todo)
	db.session.commit() #this adds a record
	return jsonify({
		'description': todo.description
	}) #we are no longer reloading the html 

@app.route('/') #sets up a route to listen to our homepage
def index():
	return render_template('index.html', data=Todo.query.all()
		)