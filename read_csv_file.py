import csv

def find_value_by_keyword(csv_file_path, keyword):
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
                        return row[i + 1].strip()
                    except IndexError:
                        print(f"Нет следующей ячейки в строке {row_num}")
                        pass
    
    return None

# Используем функцию
csv_file_path = '1_row_1262G3_2025.11.04_10.34.csv'
keyword = 'Коэффициент высоты протуберанца [hprP*]'
result = find_value_by_keyword(csv_file_path, keyword)

print("Значение:", result)
