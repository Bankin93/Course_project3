import requests
from funcs import (
    get_last_five_transactions,
    formatted_date,
    get_description,
    get_sender,
    get_recipient,
    get_amount,
    get_currency
)

URL = "https://www.jsonkeeper.com/b/KJED"


def main():
    """Основная программа"""
    list_operation = requests.get(URL).json()

    for transaction in get_last_five_transactions(list_operation):
        print(":" * 50)
        print(formatted_date(transaction), get_description(transaction))
        print(get_sender(transaction), "->", get_recipient(transaction))
        print(get_amount(transaction), get_currency(transaction))
    print(":" * 50)


if __name__ == '__main__':
    main()
