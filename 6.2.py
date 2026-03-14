from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML-шаблон в виде строки
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Flask Form</title>
</head>
<body>
    <h1>Приветствие</h1>
    {% if name %}
        <p>Привет, {{ name }}!</p>
        <a href="/">Назад</a>
    {% else %}
        <form method="post">
            <label for="name">Введите ваше имя:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Отправить</button>
        </form>
    {% endif %}
</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template_string(HTML_TEMPLATE, name=name)


if __name__ == '__main__':
    app.run(debug=True)