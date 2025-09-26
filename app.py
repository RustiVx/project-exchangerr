import requests
from credentials import api_key
from flask import Flask, render_template, request

app = Flask(__name__)

# Получение данных от пользователя
def get_user_input():
    curr_from = input('Введите исходную валюту: ').upper()
    curr_to = input('Введите целевую валюту: ').upper()
    amount = int(input('Введите сумму для конвертации: '))
    return curr_from, curr_to, amount

# Преобразование данных (конвертация)
def get_converted_amount(curr_from, curr_to, amount):

    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{curr_from}/{curr_to}/{amount}'

    data = requests.get(url).json()

    converted_amount = data['conversion_result']
    
    return converted_amount

# Вывод конвертированных данных
def get_converted_print():
    curr_from, curr_to, amount =  get_user_input()
    converted_amount = get_converted_amount(curr_from, curr_to, amount)

# Главная страница сайта
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        curr_from = request.form['curr-from'].upper()
        curr_to = request.form['curr-to'].upper()
        amount = float(request.form['amount'])
        if curr_from and curr_to and amount > 0:
            result = get_converted_amount(curr_from, curr_to, amount)
    return render_template('index.html', result=result)

# Запуск app.py
if __name__ == "__main__":
    print("Flask успешно запущен")
    app.run(debug=True)