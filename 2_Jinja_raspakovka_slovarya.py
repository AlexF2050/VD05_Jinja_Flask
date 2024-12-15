# Открытие ссылки на сайт http://127.0.0.1:5000/
# САЙТ из ПАПОК

from flask import Flask, render_template #Подключение библиотек

# Создаём переменную app в которую мы сохраняем экземпляр класса Flask с переменной __name__
app = Flask(__name__)

# Декоратор для прописывания маршрута, url адресов функциям. Одна функция работает с одной web страницей
@app.route("/") # Декоратор
def index():
    return render_template("index.html", caption="Праздники") # Возвращаем html файл

@app.route("/shablon") # Декоратор
def blog():
    context = {
        "caption": "Блог",
        "link": "Читать далее"
    }
    return render_template("blog.html", **context) # Возвращаем html файл

@app.route("/shablon2") # Декоратор
def contacts():
    return render_template("contacts.html", caption="Контакты")

# Проверяем работу приложения, запускаем его
if __name__ == "__main__":
    app.run()
