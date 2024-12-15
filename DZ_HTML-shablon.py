# Открытие ссылки на сайт http://127.0.0.1:5000/

from flask import Flask, render_template #Подключение библиотек

# Создаём переменную app в которую мы сохраняем экземпляр класса Flask с переменной __name__
app = Flask(__name__)

# Декоратор для прописывания маршрута, url адресов функциям. Одна функция работает с одной web страницей
@app.route("/") # Декоратор
def index():
    return render_template("home.html", caption="Праздники") # Возвращаем html файл

@app.route("/shablon") # Декоратор
def blog():
    context = {
        "link": "Читать далее"
    }
    return render_template("about.html", **context) # Возвращаем html файл

# Проверяем работу приложения, запускаем его
if __name__ == "__main__":
    app.run()
