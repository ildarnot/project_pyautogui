import re

def extract_data_gear_1(line):
    """Извлекает название и значение из строки для первого файла."""
    pattern = r'^(.*?\])\s+([\d.]+(?:\s*/\s*[\d.]+)?)'
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        value = match.group(2)
        return name, value
    else:
        return None, None

def extract_data_gear_output(line):
    """Извлекает название и значение из строки для второго файла."""
    pattern = r'^(.*?\])\s+([+-]?\d*\.?\d+)'
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        value = match.group(2)
        return name, value
    else:
        return None, None

def get_key(name):
    """Выделяет ключ из названия (текст в квадратных скобках)."""
    match = re.search(r'\[(.*?)\]', name)
    return match.group(1) if match else None

# --- Чтение данных из файлов ---
print('extract_data_gear_1')
gear1_records = []
with open('3 ряд_1262G3_output_2025.11.17_15.43.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            name, value = extract_data_gear_1(line)
            if name and value:
                key = get_key(name)
                gear1_records.append({'name': name, 'value': value, 'key': key})

print('extract_output_data_gear')
output_records = []
failed_lines = []
with open('3 ряд_1262G3_output_2025.11.17_15.43_2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            name, value = extract_data_gear_output(line)
            if name and value:
                key = get_key(name)
                output_records.append({'name': name, 'value': value, 'key': key})
            else:
                failed_lines.append(line)

# --- Сопоставление по точным ключам и сравнение значений ---
matched = []      # пары с совпадающими ключами и результатами сравнения
unmatched_gear1 = []  # записи из gear1 без совпадения
unmatched_output = []  # записи из output без совпадения


# Создаём словарь для быстрого поиска по ключу из output
output_dict = {rec['key']: rec for rec in output_records if rec['key']}


# Проходим по записям gear1
for rec in gear1_records:
    key = rec['key']
    if key in output_dict:
        out_rec = output_dict[key]
        # Сравниваем значения (приводим к float для числового сравнения)
        try:
            value_gear1 = float(rec['value'].replace(',', '.'))
            value_output = float(out_rec['value'].replace(',', '.'))
            if abs(value_gear1 - value_output) < 1e-9:  # учёт погрешностей float
                comparison = "Значение совпадает"
            else:
                comparison = "!Значение не совпадает!"
        except ValueError:
            # Если не удалось преобразовать в число — сравниваем как строки
            if rec['value'] == out_rec['value']:
                comparison = "Значение совпадает"
            else:
                comparison = "!Значение не совпадает!"
        matched.append((rec, out_rec, comparison))
    else:
        unmatched_gear1.append(rec)

# Находим записи из output, которых нет в gear1
output_keys = {rec['key'] for rec in output_records if rec['key']}
gear1_keys = {rec['key'] for rec in gear1_records if rec['key']}
unmatched_output_keys = output_keys - gear1_keys


for rec in output_records:
    if rec['key'] in unmatched_output_keys:
        unmatched_output.append(rec)

# --- Вывод результатов ---
print("\n" + "="*60)
print("СОВПАВШИЕ ПАРЫ (точные ключи)")
print("="*60)

for g1, out, comp in matched:
    print(f"[{g1['key']}]")
    print(f"  gear1:   {g1['name']} = {g1['value']}")
    print(f"  output:  {out['name']} = {out['value']}")
    print(f"  {comp}")
    print("-" * 60)

print("\n" + "="*60)
print("НЕСОПОСТАВЛЕННЫЕ ЗАПИСИ ИЗ GEAR_1")
print("="*60)

for rec in unmatched_gear1:
    print(f"[{rec['key']}] {rec['name']} = {rec['value']}")

print("\n" + "="*60)
print("НЕСОПОСТАВЛЕННЫЕ ЗАПИСИ ИЗ OUTPUT")
print("="*60)

for rec in unmatched_output:
    print(f"[{rec['key']}] {rec['name']} = {rec['value']}")

# --- Вывод нераспознанных строк ---
if failed_lines:
    print("\n" + "-"*60)
    print("СТРОКИ, НЕ РАСПОЗНАННЫЕ РЕГУЛЯРНЫМ ВЫРАЖЕНИЕМ")
    print("-"*60)
    for line in failed_lines:
        print(line)
else:
    print("\n--- Все строки успешно распознаны ---")
