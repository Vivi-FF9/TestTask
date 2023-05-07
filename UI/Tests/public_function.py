from Source.public_functions import datetime_comparison, csv_string_builder, datetime_to_format_str


def transaction_info_comparison(transaction_info: dict, expected: dict):
    datetime_comparison(transaction_info['Date-Time'], expected['Date-Time'])
    assert transaction_info['Amount'] == expected['Amount'], "Сумма не соответствует"
    assert transaction_info['Transaction Type'] == expected['Transaction Type'], "Тип транзакции не соответствует"


def create_transaction_csv_report_str(transaction_info_list: list[dict]) -> str:
    headers = ["Дата-времяТранзакции", "Сумма", "ТипТранзакции"]
    values = []
    for transaction_info in transaction_info_list:
        values.append([
            datetime_to_format_str(transaction_info['Date-Time']),
            transaction_info['Amount'],
            transaction_info['Transaction Type']
        ])
    return csv_string_builder(headers, values)

