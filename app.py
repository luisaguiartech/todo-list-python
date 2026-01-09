from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Cria o banco de dados se não existir
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            conn = sqlite3.connect('database.db')
            conn.execute('INSERT INTO tasks (content) VALUES (?)', (task,))
            conn.commit()
            conn.close()
        return redirect('/')
    
    # Busca todas as tarefas
    conn = sqlite3.connect('database.db')
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)