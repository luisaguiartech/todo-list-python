from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista temporária (em vez de banco de dados)
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


if __name__ == '__main__':
    app.run(debug=True)
