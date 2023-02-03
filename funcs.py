def get_last_five_transactions(data_transactions):
    """Получает пять последних выполненных операций"""
    executed_transactions = []
    for transaction in range(len(data_transactions)):
        if "state" not in data_transactions[transaction]:
            continue
        if data_transactions[transaction]["state"] == "EXECUTED":
            executed_transactions.append(data_transactions[transaction])
    executed_transactions.sort(key=lambda dates: dates["date"], reverse=True)
    return executed_transactions[:5]


def formatted_date(data_transactions):
    """Форматирование даты перевода в формате ДД.ММ.ГГГГ"""
    date_operation = data_transactions["date"].split("T")[0].split('-')
    return f'{date_operation[2]}.{date_operation[1]}.{date_operation[0]}'


def get_description(data_transactions):
    """Выводит описание перевода"""
    description = data_transactions["description"]
    return description


def get_sender(data_transactions):
    """Получаем информацию счета отправителя"""
    sender = data_transactions.get('from')
    if sender is None:
        return "Данные отправителя отсутствуют"
    if sender.split()[0] == 'Счет':
        return f"{sender.split()[0]} " + '**' + f"{sender.split()[1][-4:]}"
    else:
        sender = sender.split()
        return f"{' '.join(sender[:-1])} {sender[-1][0:4]} {sender[-1][4:6]}** **** {sender[-1][-4:]}"


def get_recipient(data_transactions):
    """Получаем информацию счета получателя"""
    recipient = data_transactions.get('to')
    if recipient is None:
        return "Данные получателя отсутствуют"
    if recipient.split()[0] == 'Счет':
        return f"{recipient.split()[0]} " + '**' + f"{recipient.split()[1][-4:]}"
    else:
        recipient = recipient.split()
        return f"{' '.join(recipient[:-1])} {recipient[-1][0:4]} {recipient[-1][4:6]}** **** {recipient[-1][-4:]}"


def get_amount(data_transactions):
    """Получаем сумму перевода"""
    amount = data_transactions['operationAmount']['amount']
    return amount


def get_currency(data_transactions):
    """Получаем валюту операции"""
    currency = data_transactions['operationAmount']['currency']['name']
    return currency
