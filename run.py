import requests

class CurrencyConverter:
    def __init__(self, base_currency, target_currency):
        self.base_currency = base_currency
        self.target_currency = target_currency

    def return_content(self):
        url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.content

    def get_exchange_rate(self):
        url = f"https://api.exchangerate-api.com/v4/latest/{self.base_currency}"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json()['rates'].get(self.target_currency, None)

    def convert_currency(self, amount):
        exchange_rate = self.get_exchange_rate()
        if exchange_rate is None:
            return None
        return amount * exchange_rate

if __name__ == '__main__':
    base_currency = input("Enter base currency: ")
    target_currency = input("Enter target currency: ")
    amount = float(input("Enter amount: "))
    
    converter = CurrencyConverter(base_currency, target_currency)
    converted_amount = converter.convert_currency(amount)
    
    if converted_amount is not None:
        print(f"{amount} {base_currency} is {converted_amount} {target_currency}")
    else:
        print("Error in fetching the exchange rate.")
