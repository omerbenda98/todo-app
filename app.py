from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

todos = {
    "test1": True,  
    "test2": True,
    "test3": False   
}

@app.route('/')
def index():
    return redirect(url_for('todo_list'))

@app.route('/todos')
def todo_list():
    return render_template('todos.html', todos=todos)

@app.route('/toggle_todo/<todo_text>')
def toggle_todo(todo_text):
    if todo_text in todos:
        todos[todo_text] = not todos[todo_text]  
    return redirect(url_for('todo_list'))

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_text = request.form.get('todo_text')
    if todo_text and todo_text not in todos:
        todos[todo_text] = True  
    return redirect(url_for('todo_list'))

@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    todo_text = request.form.get('todo_text')
    if todo_text in todos:
        del todos[todo_text]
    return redirect(url_for('todo_list'))


if __name__ == '__main__':
    app.run()
