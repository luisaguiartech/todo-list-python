from flask import Flask, render_template, request, redirect
import os  # <-- Importe o módulo os (muito importante!)

app = Flask(__name__)

# Lista temporária para armazenar tarefas (em vez de banco de dados)
tasks = []


@app.route('/', methods=['GET', 'POST'])
def index():
    global tasks
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append(task)
        return redirect('/')
    return render_template('index.html', tasks=tasks)


@app.route('/healthz')
def health():
    """Rota usada pelo Render para verificar se o app está vivo."""
    return "OK", 200


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa a porta do Render
    # Escuta em todas as interfaces
    app.run(host='0.0.0.0', port=port, debug=True)
