import sys
import pdfplumber
import re
import csv
import os
from datetime import datetime

# Список PDF-файлов для обработки
pdf_files = [
    '1 ряд_1262G3.pdf',
    '2 ряд_1262G3.pdf',
    '3 ряд_1262G3.pdf',
    # '4 ряд_1262G3.pdf', #Есть 3 колеса в отчёте, не очень удобен для сравнения результатов, скорее всего
    '5 ряд_1262G3.pdf'
]

# Список слов, которые требуются для ввода в программу
words_to_find2 = [
'[mn]', 
'[z]', 
'Направление наклона', 
'[β]', 
'Данные для финишной обработки [x]', 
'[b]', 
'[αn]', 
'Высота головки зуба, исходный контур [haP*]',
'Высота ножки зуба исходного контура [hfP*]',
'Радиус ножки зуба исходного контура [ρfP*]',
'[hprP*]',
'Угол профиля протуберанца (°) [αprP]'
]

# Список слов, которые являются выводом из программы
words_to_find3 = [
'[pr0]',
'[d]',
'[αt]',
'[db]',
'[da]',
'[df]',
'[dNf]',
'[βb]',
'[k]',
'[Wk.e/i]',
'[ha]',
'[sc.e/i]',
'[san]',
'[DMeff]',
'[MdK]'
]

def process_pdf_file(pdf_file):
    # Функция поиска слов в pdf
    def find_all_words_in_pdf(pdf_path, words_list):
        results = {word: [] for word in words_list}
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    for line in text.split('\n'):
                        for word in words_list:
                            if word in line:
                                results[word].append((page_num + 1, line.strip()))
        return results


    # Перевод данных в csv

    def extract_key_and_values(line):
        # Находим часть до и включая ']'
        key_match = re.search(r'.*?\]', line)
        if not key_match:
            return None, None, None
        key = key_match.group(0)
        
        # Ищем числа ТОЛЬКО после ключа
        key_end = key_match.end()
        rest_of_line = line[key_end:].strip()
        
        # Регулярное выражение для чисел (целые, дробные, с минусом)
        numbers = re.findall(r'-?\d+\.?\d*', rest_of_line)
        
        gear1 = numbers[0] if len(numbers) >= 1 else ''
        gear2 = numbers[1] if len(numbers) >= 2 else ''
        
        return key, gear1, gear2











    def save_to_csv(results2, results3, output_csv):
        with open(output_csv, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['Строка и параметр', 'Колесо 1', 'Колесо 2'])
            # 2. Метка "Вводные данные"
            writer.writerow(['Данные из отчётов KISSoft', '---', '---'])
            writer.writerow(['Вводные данные', '---', '---'])
            
            for word, lines in results2.items():
                for page_number, line in lines:
                    key, gear1, gear2 = extract_key_and_values(line)
                    if key is not None:
                        # Форматируем числа: заключаем в кавычки и добавляем знак =
                        gear1_formatted = f'="{gear1}"' if gear1 else ''
                        gear2_formatted = f'="{gear2}"' if gear2 else ''
                        writer.writerow([key, gear1_formatted, gear2_formatted])

            # 4. Метка "Выходные данные"
            writer.writerow(['Выходные данные', '---', '---'])

            for word, lines in results3.items():
                for page_number, line in lines:
                    key, gear1, gear2 = extract_key_and_values(line)
                    if key is not None:
                        # Форматируем числа: заключаем в кавычки и добавляем знак =
                        gear1_formatted = f'="{gear1}"' if gear1 else ''
                        gear2_formatted = f'="{gear2}"' if gear2 else ''
                        writer.writerow([key, gear1_formatted, gear2_formatted])


    # Получаем имя файла без расширения
    pdf_filename_without_ext = os.path.splitext(os.path.basename(pdf_file))[0]

    # Получаем текущую дату и время в формате ГГГГ.ММ.ДД_ЧЧ.ММ
    timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M')

    # Формируем итоговое имя текстового файла
    txt_filename = f'{pdf_filename_without_ext}_output_{timestamp}.txt'

    # Открытие текстового файла для записи
    with open(txt_filename, 'w', encoding='utf-8') as txt_output:
        # Перенаправляем стандартный вывод в файл
        original_stdout = sys.stdout
        sys.stdout = txt_output
        
        try:
            print('_______Список слов, которые требуются для ввода в программу_______')

            results2 = find_all_words_in_pdf(pdf_file, words_to_find2)

            # Специальная обработка для [hprP*]: накапливаем значения
            hpr_values = []

            # Накопление значений для "Данные для финишной обработки [x]"
            x_values = []  # <-- Новый список для сбора значений [x]

            for word, lines in results2.items():
                if word == '[hprP*]':
                    # Собираем все числа из всех строк с [hprP*]
                    for page_number, line in lines:
                        key, g1, g2 = extract_key_and_values(line)
                        if g1:
                            hpr_values.append(g1)
                        if g2:
                            hpr_values.append(g2)
                elif word == 'Данные для финишной обработки [x]':
                    # Собираем значения, не выводим сразу
                    for page_number, line in lines:
                        key, g1, g2 = extract_key_and_values(line)
                        if g1:
                            x_values.append(g1)
                        if g2:
                            x_values.append(g2)
                else:
                    # Для остальных параметров — обычный вывод
                    for page_number, line in lines:
                        print(line)

            # Теперь выводим [hprP*] группами по 2 значения (или по 1, если осталось нечётное)
            print(f"Коэффициент высоты протуберанца [hprP*]", end="")
            for i, val in enumerate(hpr_values):
                if i > 0 and i % 2 == 0:  # Каждые 2 значения — новая строка
                    print()  # Переход на новую строку
                    print(f"Коэффициент высоты протуберанца [hprP*]", end="")
                print(f" {val}", end="")
            if hpr_values:  # Если были значения — завершаем строку
                print()  # Перевод строки

            # Выводим "Данные для финишной обработки [x]" одной строкой
            if x_values:
                print(f"Данные для финишной обработки [x] {' '.join(x_values)}")
            
            print('_______Список выходных данных_______')

            # Проводим поиск всех слов сразу
            results3 = find_all_words_in_pdf(pdf_file, words_to_find3)

            # Используем словарь для накопления уникальных значений
            accumulated_values = {
                '[pr0]': [],
                '[d]': [],
                '[db]': [],
                '[da]': [],
                '[df]': [],  # Включили сюда также [df]
                '[san]': [],
                '[dNf]': [],
            }

            # Отдельно накапливаем значения для [ha] без префикса
            ha_values = []

            # Собираем все нужные значения в один проход
            for word, lines in results3.items():
                if word in accumulated_values.keys():  # Только интересующие нас ключи
                    for _, line in lines:
                        key, gear1, gear2 = extract_key_and_values(line)
                        if gear1:
                            accumulated_values[word].append(gear1)
                        if gear2:
                            accumulated_values[word].append(gear2)
                elif word == '[ha]':
                    for _, line in lines:
                        # Проверяем, есть ли префикс "Высота по хорде..."
                        if 'Высота по хорде от da.m (мм)' not in line:
                            # Это простое [ha] — накапливаем значения
                            key, gear1, gear2 = extract_key_and_values(line)
                            if gear1:
                                ha_values.append(gear1)
                            if gear2:
                                ha_values.append(gear2)
                        else:
                            # Это строка с префиксом — оставляем для прямого вывода
                            pass  # Будем выводить позже

            # Отображаем собранные значения в нужном формате
            for key, values in accumulated_values.items():
                if values:
                    label_map = {
                        '[pr0]': 'Протуберанец (мм)',
                        '[d]': 'Диаметр делительной окружности (мм)',
                        '[db]': 'Диаметр основной окружности (мм)',
                        '[da]': 'Диаметр окружности вершин зубьев (мм)',
                        '[df]': 'Диаметр окружности впадин (мм)',
                        '[san]': 'Нормальная толщина зуба на окружности вершин зубьев (мм)',
                        '[dNf]': 'Диаметр окружности нижних активных точек профиля (мм)'
                    }
                    label = label_map.get(key, '')
                    print(f"{label} {key} {' '.join(values)}")

            # Выводим [ha] одной строкой (если есть значения)
            if ha_values:
                print(f"[ha] {' '.join(ha_values)}")

            # Остальной вывод оставшихся элементов (включая [ha] с префиксом)
            remaining_keys = set(words_to_find3) - set(accumulated_values.keys())
            for word in remaining_keys:
                if word in results3:
                    for _, line in results3[word]:
                        # Выводим только строки с префиксом для [ha]
                        if word == '[ha]' and 'Высота по хорде от da.m (мм)' in line:
                            print(line)
                        # Для остальных слов — выводим всё
                        elif word != '[ha]':
                            print(line)
        finally:
            # Восстанавливаем стандартный вывод обратно в терминал
            sys.stdout = original_stdout


    # Сохраняем в CSV

    # 1. Получаем имя файла без расширения
    pdf_filename_without_ext = os.path.splitext(os.path.basename(pdf_file))[0]

    # 2. Получаем текущую дату и время в формате ГГГГММДД_ЧЧММСС
    timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M')

    # 3. Формируем итоговое имя CSV-файла
    csv_filename = f'{pdf_filename_without_ext}_{timestamp}.csv'

    # 4. Сохраняем в CSV с новым именем
    # save_to_csv(results2, results3, csv_filename)
    return txt_filename

# Основной цикл обработки
all_txt_files = []
# all_csv_files = []

for pdf_file in pdf_files:
    print(f"Обработка файла: {pdf_file}")
    txt_file = process_pdf_file(pdf_file)
    # txt_file, csv_file = process_pdf_file(pdf_file)
    all_txt_files.append(txt_file)
    # all_csv_files.append(csv_file)

print("Обработка завершена. Созданы файлы:")
for txt in all_txt_files:
    print(f"TXT: {txt}")
# for csv in all_csv_files:
#     print(f"CSV: {csv}")