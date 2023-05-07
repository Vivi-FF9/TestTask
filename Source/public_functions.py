from datetime import datetime, timedelta


def get_today_fibonacci_num() -> int:
    # Возвращает значение n-ое число Фибоначчи, где n это сегодняшнее число + 1
    first_32_fibonacci_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
                               10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
    today_num = datetime.today().day
    return first_32_fibonacci_nums[today_num]


def str_to_datetime_object(str_datetime: str) -> datetime:
    # "May 7, 2023 1:05:28 PM" -> datetime
    return datetime.strptime(str_datetime, '%B %d, %Y %I:%M:%S %p')


def datetime_to_format_str(datetime_obj: datetime) -> str:
    # datetime -> "07 May 2023 13:05:28"
    return datetime_obj.strftime('%d %B %Y %H:%M:%S')


def get_now_datetime() -> datetime:
    return datetime.now()


def datetime_comparison(dt_1: datetime, dt_2: datetime, allow_difference_sec: float = 1.5) -> None:
    # Проверка на то, что разница во времени не более allow_difference_sec секунд
    allow_difference = timedelta(seconds=allow_difference_sec)
    if dt_1 >= dt_2:
        difference = dt_1 - dt_2
    else:
        difference = dt_2 - dt_1
    assert difference <= allow_difference, f"разница во времени {difference}, допустимая {allow_difference_sec} секунд"


def csv_string_builder(headers: list[str], values: list[list[str]], sep: str = ',', newline: str = '\r\n') -> str:
    # Формирование csv файла в виде строки
    header_str = f"{sep.join(headers)}{newline}"
    body_str = ''
    for row in values:
        body_str += f"{sep.join(row)}{newline}"
    return header_str + body_str

