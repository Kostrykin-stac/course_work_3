import json
from datetime import datetime


def load_operations(file_name):
    """Функция загрузки данных из JSON-файла"""
    with open(file_name, 'r') as file:
        operations = json.load(file)
    return operations


def display_recent_operations(file_name):
    """Функция отображающая информации о недавних операциях"""
    operations = load_operations(file_name)
    executed_operations = filter_executed_operations(operations)
    sorted_operations = sort_operations_by_date(executed_operations)
    display_operations_info(sorted_operations)


def filter_executed_operations(operations):
    """Функция фильтрующая выполненные операций"""
    executed_operations = []
    for op in operations:
        if op.get('state') == 'EXECUTED':
            executed_operations.append(op)
    return executed_operations


def sort_operations_by_date(operations):
    """Функция сортировки операций по дате"""
    return sorted(operations, key=lambda op: datetime.strptime(op['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)


def display_operations_info(operations):
    """Функция отображающая информации об операциях"""
    for operation in operations[:5]:
        date = operation['date']
        parsed_date = datetime.fromisoformat(date)
        formatted_date = parsed_date.strftime("%d.%m.%Y")
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['code']
        description = operation['description']
        from_account = operation.get('from', "N/A")
        to_account = operation.get('to', "N/A")
        masked_from_account = masking_card(from_account)
        masked_to_account = mask_account_number(to_account)
        print(f"{formatted_date} {description}\n{masked_from_account} -> {masked_to_account}\n{amount} {currency}\n")


def masking_card(card_info: str):
    """Функция маскировки информации о карте/счете"""
    if len(card_info) != 0:
        card_number = card_info.split()[-1]
        card_name = ' '.join(card_info.split()[:-1])

        if len(card_number) == 16 and card_number.isdigit():
            card_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]

        elif len(card_number) == 20 and card_number.isdigit():
            card_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]

        else:
            return 'Uncorrected card_info'

        return f'{card_name} {card_number}'

    return ''


def mask_account_number(account_number):
    """Функция маскировки номера счета"""
    masked_number = account_number[:4] + ' ' + "**" + account_number[-4:]
    return masked_number


file_name = '/home/maxim/PycharmProjects/course_work_3/operations.json'
"""Путь к файлу с операциями"""
display_recent_operations(file_name)
