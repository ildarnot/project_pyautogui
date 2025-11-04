import csv

def find_value_by_keyword(csv_file_path, keyword, occurrence=1):
    """
    Находит значение по ключевому слову в CSV.
    
    Параметры:
    - csv_file_path: путь к CSV-файлу
    - keyword: искомое ключевое слово
    - occurrence: номер вхождения (1 = первое, 2 = второе, 3 = третье и т. д.)
    
    Возвращает:
    - Значение из соседней ячейки или None, если не найдено
    """
    matches = []  # Список для хранения всех найденных значений
    
    with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        
        for row_num, row in enumerate(reader):
            # Пропускаем пустые строки
            if not row or not any(cell.strip() for cell in row):
                continue
            
            for i, cell in enumerate(row):
                # Проверяем наличие ключевого слова (без учёта регистра и пробелов)
                if keyword.lower() in cell.strip().lower():
                    # Берём соседнюю ячейку справа
                    try:
                        value = row[i + 1].strip()
                        matches.append(value)
                    except IndexError:
                        print(f"Нет следующей ячейки в строке {row_num + 1}")
    
    # Возвращаем нужное вхождение (если существует)
    if len(matches) >= occurrence:
        return matches[occurrence - 1]  # Индексация с 0
    else:
        print(f"Не найдено {occurrence}-го вхождения ключевого слова.")
        return None

# Используем функцию
csv_file_path = '1_row_1262G3_2025.11.04_10.34.csv'
keyword = '[hprP*]'
result = find_value_by_keyword(csv_file_path, keyword, occurrence=3)  # Третий результат

print("Значение:", result)
