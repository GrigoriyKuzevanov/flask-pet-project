from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'Платежные Документы', 'url': '/documents/'},
    {'name': 'Тарифы', 'url': '/prices/'},
    {'name': 'Статистика', 'url': '/stats/'}
]


@app.route('/')
def index():
    url = url_for('index')
    return render_template('index.html', menu=menu, url=url)

@app.route('/documents/')
def documents():
    url = url_for('documents')
    return render_template('documents.html', title='Платежные документы', menu=menu, url=url)

@app.route('/documents/<doc_num>/')  # конвертеры: path, int, float (<int:doc_num>)
def show_document(doc_num):
    return f'Пользователь: {doc_num}'

@app.route('/prices/', methods=['POST', 'GET'])
def prices():
    url = url_for('prices')
    if request.method == 'POST':
        print(request.form)
    return render_template('prices.html', title='Тарифы', menu=menu, url=url)

@app.route('/stats/')
def stats():
    url = url_for('stats')
    return render_template('stats.html', title='Статистика', menu=menu, url=url)

# with app.test_request_context():
#     print(url_for('about'))
#     print(url_for('profile', username='grigoriy'))

if __name__ == '__main__':
    app.run(debug=True)
