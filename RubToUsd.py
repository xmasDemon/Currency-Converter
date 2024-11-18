import requests


def get_exchange_rates():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    return data['rates']['RUB'], data['rates']['USD']


def convert_currency(amount, rate):
    return amount * rate


def main():
    rub_to_usd, usd_to_rub = get_exchange_rates()
    print(f"Курс: 1 USD = {rub_to_usd} RUB, 1 RUB = {usd_to_rub} USD")

    while True:
        currency = input(
            "Введите 'R' для конвертации рублей в доллары, 'D' для доллара в рубли или 'Q' для выхода: ").strip().upper()
        if currency == 'Q':
            break
        amount = float(input("Введите сумму для конвертации: "))

        if currency == 'R':
            result = convert_currency(amount / rub_to_usd, 1)
            print(f"{amount} RUB = {result:.2f} USD")
        elif currency == 'D':
            result = convert_currency(amount * rub_to_usd, 1)
            print(f"{amount} USD = {result:.2f} RUB")
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()