from . import jalali
from django.utils import timezone


# this method converts english numbers tp persian numbers
def persian_numbers(input: str):
    numbers = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹'
    }

    for english_number, persian_number in numbers.items():
        input = input.replace(english_number, persian_number)
    return input


# this method converts gregorian date to jalali date
def jalali_converter(time):
    jalali_months = [
        'فروردین',
        'اردیبهشت',
        'خرداد',
        'تیر',
        'مرداد',
        'شهریور',
        'مهر',
        'آبان',
        'آذر',
        'دی',
        'بهمن',
        'اسفند']
    time = timezone.localtime(time)
    time_to_str = f'{time.year},{time.month},{time.day}'
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jalali_months):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
    hour = 'ساعت'
    new_time = f'{time_to_list[0]}'
    return persian_numbers(new_time)
