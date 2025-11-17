# Выгрузка данных из txt

import re
import csv
import os

input_filename = '2_row_1262_05.11.2025_09.38.txt'
# Удаляем расширение и добавляем .csv
output_filename = os.path.splitext(input_filename)[0] + '.csv'

def parse_line(line):
    line = line.strip()
    if not line:
        return None, None

    # Улучшенный шаблон для поиска чисел (исключает даты)
    match = re.search(r'-?(?:\d{1,2}(?![.\d])|\d+)(?:[,.]\d+)?(?![.\d])', line)
    if not match:
        return line, None

    num_start = match.start()
    keyword = line[:num_start].strip()
    number_str = match.group()

    # Заменяем запятую на точку для float
    number_str = number_str.replace(',', '.')

    try:
        result = float(number_str)
    except ValueError:
        result = None

    return keyword, result

def main():


    try:
        with open(input_filename, 'r', encoding='utf-8-sig') as infile, \
             open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:

            writer = csv.writer(outfile, delimiter=';')
            writer.writerow(['Строка и параметр', 'Колесо 1'])

            for line_num, line in enumerate(infile, 1):
                keyword, result = parse_line(line)

                if keyword is not None:
                    if result is not None:
                        # Формируем строку с явным указанием формата числа
                        value_str = f'{result:.3f}'  # 3 знака после запятой
                    else:
                        value_str = ''

                    writer.writerow([keyword, value_str])

                    print(f'Строка {line_num}:')
                    print(f'  Ключевое слово: "{keyword}"')
                    if result is not None:
                        print(f'  Результат (число): {result}')
                    else:
                        print(f'  Результат: не найдено числовое значение')
                    print()

        print(f'Данные успешно записаны в файл "{output_filename}".')

    except FileNotFoundError:
        print(f'Ошибка: файл "{input_filename}" не найден.')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

if __name__ == '__main__':
    main()