from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(
    os.getenv('MYSQL_USER', 'todo_user'),
    os.getenv('MYSQL_PASSWORD', 'todo_pass'),
    os.getenv('MYSQL_HOST', 'db'),
    os.getenv('MYSQL_DATABASE', 'todo_db')
)
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), unique=True, nullable=False)
    completed = db.Column(db.Boolean, default=True)

# Initialize database (create tables)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('todo_list'))

@app.route('/todos')
def todo_list():
    todos = {todo.text: todo.completed for todo in Todo.query.all()}
    return render_template('todos.html', todos=todos)

@app.route('/toggle_todo/<todo_text>')
def toggle_todo(todo_text):
    todo = Todo.query.filter_by(text=todo_text).first()
    if todo:
        todo.completed = not todo.completed
        db.session.commit()
    return redirect(url_for('todo_list'))

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_text = request.form.get('todo_text')
    if todo_text:
        existing_todo = Todo.query.filter_by(text=todo_text).first()
        if not existing_todo:
            new_todo = Todo(text=todo_text)
            db.session.add(new_todo)
            db.session.commit()
    return redirect(url_for('todo_list'))

@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    todo_text = request.form.get('todo_text')
    todo = Todo.query.filter_by(text=todo_text).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('todo_list'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)