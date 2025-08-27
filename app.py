from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

todo_list = ["파이썬 공부하기", "운동하기"]

@app.route('/')
def home():
    return redirect(url_for('todo_list_page'))

@app.route('/todo')
def todo_list_page():
    return render_template('todo.html', todo_list=todo_list)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_item = request.form.get('todo_item')
    if todo_item:
        todo_list.append(todo_item)
    return redirect(url_for('todo_list_page'))

if __name__ == '__main__':
    app.run(debug=True)