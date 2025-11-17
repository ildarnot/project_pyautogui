import csv
import os
import chardet
from datetime import datetime

# Явное сопоставление ключей: ключ_из_PDF → ключ_из_TXT
MAPPING = {
    '[mn]': 'Модуль m, мм',
    '[z]': 'Число зубьев z, шт.',
    '[β]': 'Угол наклона линии зубьев β, °',
    'Данные для финишной обработки [x]': 'Коэффициент смещения x',
    '[b]': 'Ширина, мм',
    '[αn]': 'Исходный профиль	Угол профиля α, °:',
    '[haP*]': 'Коэффициент высоты головки ha*:',
    '[hfP*]': 'Коэффициент высоты ножки hf*:',
    '[ρfP*]': 'Коэффициент радиуса кривизны переходной кривой r*:',
    '[hprP*]': 'Коэффициент высоты протуберанца h_pr',
    '[pr0]':'Протуберанец pr',
    '[αprP]' : 'Угол протуберанца α_pr, °:',
    '[pr0]': 'Коэффициент высоты протуберанца h_pr:',
    '[d]': 'Делительный диаметр, мм',
    '[αt]': 'Угол профиля торцевой, °',
    '[db]': 'Основной диаметр, мм',
    '[da]': 'Диаметр вершин, мм',
    '[df]': 'Диаметр впадин, мм'
}

# Функция для автоматического определения кодировки
def detect_encoding(file_path):
    raw_data = open(file_path, 'rb').read()
    detected_result = chardet.detect(raw_data)
    return detected_result['encoding']

# Чтение CSV-файлов и возврат полного списка записей
def read_csv(filename):
    encoding = detect_encoding(filename)
    records = []
    try:
        with open(filename, 'r', encoding=encoding) as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)  # Пропускаем заголовок
            for row in reader:
                if len(row) > 1:
                    record = {'key': row[0].strip(), 'value': row[1].strip()}
                    records.append(record)
    except FileNotFoundError:
        print(f"Файл не найден: {filename}")
    return records

def merge_data(pdf_csv, txt_csv, output_csv):
    # Читаем данные
    pdf_records = read_csv(pdf_csv)
    txt_records = read_csv(txt_csv)

    # Формируем итоговый CSV
    with open(output_csv, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        # Заголовок
        writer.writerow([
            'Параметр (PDF)', 'Значение (PDF)',
            'Параметр (TXT)', 'Значение (TXT)'
        ])

        # Проходим по записям из PDF и пытаемся сопоставить с TXT
        for pdf_record in pdf_records:
            pdf_key = pdf_record['key']  # Полностью считанный ключ из PDF
            pdf_value = pdf_record['value']

            # Пробуем найти сопоставление в MAP
            mapped_txt_key = ''
            for map_pdf_key, map_txt_key in MAPPING.items():
                if map_pdf_key in pdf_key:
                    mapped_txt_key = map_txt_key
                    break

            # Поиск значения из TXT
            matched_txt_value = ''
            for txt_rec in txt_records:
                if txt_rec['key'] == mapped_txt_key:
                    matched_txt_value = txt_rec['value']
                    break

            writer.writerow([pdf_key, pdf_value, mapped_txt_key, matched_txt_value])

# if __name__ == '__main__':
#     # Имена файлов (настройте под свои)
#     PDF_CSV = '1_row_1262G3_2025.11.04_13.35.csv'  # Выход pdf_to_csv
#     TXT_CSV = '1_row_1262G3.csv'                   # Выход txt_to_csv
#     OUTPUT_CSV = 'merged_output.csv'

#     merge_data(PDF_CSV, TXT_CSV, OUTPUT_CSV)
#     print(f"Итоговый файл создан: {OUTPUT_CSV}")
if __name__ == '__main__':

    # 2. Получаем текущую дату и время в формате ГГГГММДД_ЧЧММСС
    timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M')
    # Имена файлов (настройте под свои)
    PDF_CSV = '5 ряд_1262G3_2025.11.04_15.26.csv'  # Выход pdf_to_csv
    TXT_CSV = '5_row_1262_04.11.2025_15.45.csv'                   # Выход txt_to_csv
    OUTPUT_CSV = f'5_row_merged_{timestamp}.csv'

    merge_data(PDF_CSV, TXT_CSV, OUTPUT_CSV)
    print(f"Итоговый файл создан: {OUTPUT_CSV}")
