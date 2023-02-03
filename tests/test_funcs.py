import pytest
from funcs import (
    get_last_five_transactions,
    formatted_date,
    get_description,
    get_sender,
    get_recipient,
    get_amount,
    get_currency
)


@pytest.fixture
def list_transactions():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }]


@pytest.fixture
def executed_transaction():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }]


def test_get_last_five_transactions(list_transactions, executed_transaction):
    assert get_last_five_transactions([{}]) == []
    assert get_last_five_transactions(list_transactions) == executed_transaction


def test_formatted_date():
    assert formatted_date({'date': '2020-04-24T02:08:58.425572'}) == '24.04.2020'


def test_get_description():
    assert get_description({'description': 'Перевод с карты на счет'}) == 'Перевод с карты на счет'


def test_get_sender():
    assert get_sender({'from': 'Visa Classic 7022985698476865'}) == 'Visa Classic 7022 98** **** 6865'
    assert get_sender({'not': '23'}) == 'Данные отправителя отсутствуют'
    assert get_sender({}) == 'Данные отправителя отсутствуют'
    assert get_sender({'from': 'Счет 75743795418434298755'}) == 'Счет **8755'
    assert get_sender({'from': 'Cчет'}) == ' Cчет ** **** Cчет'

def test_get_recipient():
    assert get_recipient({'to': 'Счет 60979028617970883410'}) == 'Счет **3410'
    assert get_recipient({'to': 'Cчет'}) == ' Cчет ** **** Cчет'
    assert get_recipient({}) == 'Данные получателя отсутствуют'
    assert get_recipient({'to': 'Visa Classic 7022985698476865'}) == 'Visa Classic 7022 98** **** 6865'
    assert get_recipient({'from': 'Visa Classic 7022985698476865'}) == 'Данные получателя отсутствуют'


def test_get_amount():
    assert get_amount({'operationAmount': {'amount': '16872.46'}}) == '16872.46'


def test_get_currency():
    assert get_currency({'operationAmount': {'currency': {'name': 'USD'}}}) == 'USD'
