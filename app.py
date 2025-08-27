from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('todo_list'))

# 새로운 라우트 추가
@app.route('/todo')
def todo_list():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True)