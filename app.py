from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    features = [
        {
            "title": "Быстрый запуск",
            "text": "Установка и запуск за несколько минут без лишних действий."
        },
        {
            "title": "Удобная панель",
            "text": "Минималистичный интерфейс с понятной структурой разделов."
        },
        {
            "title": "Поддержка 24/7",
            "text": "Оперативная помощь и ответы на основные вопросы."
        }
    ]

    plans = [
        {
            "name": "Base",
            "price": "7 390 ₽",
            "items": ["1 устройство", "Базовый доступ", "Стартовая поддержка"]
        },
        {
            "name": "Pro",
            "price": "19 990 ₽",
            "items": ["До 5 устройств", "Расширенные функции", "Приоритетная поддержка"]
        }
    ]

    return render_template("index.html", features=features, plans=plans)

if __name__ == "__main__":
    app.run(debug=True)
