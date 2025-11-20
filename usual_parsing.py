import re

# Выгрузка данных из вводного txt "3 ряд_1262G3_output_2025.11.17_15.43.txt" для первого колеса
def extract_data_gear_1(line):
    pattern = r'^(.*?\])\s+([-+]?[\d.]+(?:\s*/\s*[\d.]+)?)'
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        value = match.group(2)
        return name, value
    else:
        failed_lines.append(line)  # Запоминаем строку, не подошедшую под шаблон
        return None, None

# Примеры использования
print("\n"+"="*60)
print('Вводные данные extract_data_gear_1')
print("="*60)
input_1_lines = []
failed_lines = []
with open('3 ряд_1262G3_output_2025.11.17_15.43.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # пропускаем пустые строки
            input_1_lines.append(line.strip())

for line in input_1_lines:
    input_1_name, input_1_value = extract_data_gear_1(line)
    print(f"input 1 {input_1_name} |{input_1_value}")

# Выводим строки, не совпавшие с шаблоном
if failed_lines:
    print("\n--- Строки, не совпавшие с регулярным выражением Вводные данные extract_data_gear_1 ---")
    for failed_line in failed_lines:
        print(failed_line)
else:
    print("\n--- Все строки успешно распознаны ---")



# Попытка воспользоваться старым кодом для выписывания текста из итогового документа
def extract_data_gear_output(line):
    # Обновлённый шаблон:
    # - (.*?\]) — захватываем название до ]
    # - \s+ — любые пробельные символы (пробелы, табуляции)
    # - ([+-]?\d*\.?\d+) — число (с возможным знаком +/-, целой и дробной частью)
    pattern = r'^(.*?\])\s+([+-]?\d*\.?\d+)'
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        value = match.group(2)
        return name, value
    else:
        failed_lines.append(line)  # Запоминаем строку, не подошедшую под шаблон
        return None, None
    
print("\n"+"="*60)
print('Выходные данные extract_output_data_gear')
print("="*60)
output_1_lines = []
failed_lines = []
with open('3 ряд_1262G3_output_2025.11.17_15.43_2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # пропускаем пустые строки
            output_1_lines.append(line.strip())

for line in output_1_lines:
    name, value = extract_data_gear_output(line)
    print(f"output 1 {name} |{value}")

# Выводим строки, не совпавшие с шаблоном
if failed_lines:
    print("\n--- Строки, не совпавшие с регулярным выражением Выходные данные extract_output_data_gear ---")
    for failed_line in failed_lines:
        print(failed_line)
else:
    print("\n--- Все строки успешно распознаны ---")


# # Выгрузка данных из вводного txt "3 ряд_1262G3_output_2025.11.17_15.43.txt" для второго колеса
# print("\n"+"="*60)
# print('extract_data_gear_2')
# print("="*60)
# def extract_data_gear_2(line):
#     # Ищем всё от начала строки до ] включительно — это название
#     bracket_match = re.search(r'^.*?\]', line)
#     if not bracket_match:
#         return None, None  # Если скобки ] нет — не обрабатываем
    
#     name = bracket_match.group(0)  # Само совпадение (всё до ] включительно)
    
#     # Остаток строки после названия
#     rest = line[len(name):].strip()
    
#     # Находим ВСЕ числовые фрагменты (числа с точкой, возможно разделённые /)
#     # Шаблон: число (\d+\.?\d*), затем возможно / и снова число — повторяется
#     number_groups = re.findall(r'\d+\.?\d*(?:\s*/\s*\d+\.?\d*)*', rest)
    
#     if not number_groups:
#         return name, None  # Нет чисел — значение None
    
#     # Берём ПОСЛЕДНЮЮ найденную группу чисел
#     value = number_groups[-1]
    
#     return name, value.strip()

# # Примеры использования
# lines = []
# with open('3 ряд_1262G3_output_2025.11.17_15.43.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         if line.strip():  # пропускаем пустые строки
#             lines.append(line.strip())

# for line in lines:
#     name, value = extract_data_gear_2(line)
#     print(f"input 2 {name} |{value}")


# Получаем список кортежей сразу, это наша база, откуда мы тащим значения для маппинга
input_1_results = list(map(extract_data_gear_1, input_1_lines))
output_1_results = list(map(extract_data_gear_output, output_1_lines))

# # Выводим все результаты
# for name, value in input_1_results:
#     print(f"input 1 {name} |{value}")
    
# Маппинг
mapping = {
    '[mn]': '[mn]',
    '[z]': '[z]',
    '[β]': '[β]',
    '[b]': '[b]',
    '[αn]': '[α]',
    '[haP*]': '[ha*]',
    '[hfP*]': '[hf*]',
    '[ρfP*]': '[r*]',
    '[αprP]': '[α_pr]',
    '[hprP*]': '[h_pr]',
    '[x]': '[x]',
    '[pr0]': '[pr0]',
    '[d]': '[d]',
    '[db]': '[db]',
    '[da]': '[da]',
    '[df]': '[df]',
    '[san]': '[san]',
    '[βb]': '[βb]',
    '[MdK]': '[MdK]',
    '[DMeff]': '[DMeff]',
    '[k]': '[k]',
    '[αt]': '[αt]',
    '[ha]': '[ha]',
    '[Wk.e/i]': '[Wk]',
    '[sc.e/i]': '[sc]'
}


def combine_data(input_data, output_data, mapping):
    results = []
    reverse_mapping = {v: k for k, v in mapping.items()}
    
    total_pairs = 0      # Общее число проверенных пар
    error_count = 0    # Число ошибок

    for in_name, in_value in input_data:
        if in_name is None:
            continue

        in_key_match = re.search(r'\[[^\]]+\]', in_name)
        if not in_key_match:
            continue
        in_key = in_key_match.group(0)

        if in_key not in mapping:
            continue
        expected_out_key = mapping[in_key]

        found_match = False
        for out_name, out_value in output_data:
            if out_name is None:
                continue
            out_key_match = re.search(r'\[[^\]]+\]', out_name)
            if out_key_match and out_key_match.group(0) == expected_out_key:
                found_match = True
                total_pairs += 1  # Увеличиваем счётчик пар

                # Приводим к числам и сравниваем с учётом погрешности
                try:
                    in_num = float(in_value)
                    out_num = float(out_value)
                    if abs(in_num - out_num) < 1e-9:
                        status = "Done"
                    else:
                        status = "Error"
                except (ValueError, TypeError):
                    # Если не число — сравниваем как строки
                    if in_value == out_value:
                        status = "Done"
                    else:
                        status = "Error"

                if status == "Error":
                    error_count += 1  # Увеличиваем счётчик ошибок

                line = f"{status}|input 1 {in_name} |output 1 {out_name} |{in_value} | {out_value}"
                results.append(line)
                break

        if not found_match:
            total_pairs += 1  # Учитываем отсутствующие пары как ошибки
            error_count += 1

            has_expected_key = any(
                re.search(r'\[[^\]]+\]', out_name) and
                re.search(r'\[[^\]]+\]', out_name).group(0) == expected_out_key
                for out_name, _ in output_data if out_name is not None
            )
            
            if has_expected_key:
                line = f"Error|input 1 {in_name} |output 1 [not_found] |{in_value} | [missing]"
            else:
                line = f"Error|input 1 {in_name} |output 1 [key_not_in_output] |{in_value} | [not_present]"
            
            results.append(line)

    # Добавляем итоговую статистику
    negative_percentage=100*error_count/total_pairs
    x="\n"+"="*60
    summary = f''' 
{x}
Проверено {total_pairs} пар значений, из них не совпадает {error_count}, процент несовпадения {negative_percentage} %
{x}'''
    results.append(summary)
    return results


# Пример сбора данных (как в вашем коде)

# Объединяем
combined_lines = combine_data(input_1_results, output_1_results, mapping)

# Выводим результат
print("\n" + "="*80)
print("СОПОСТАВЛЕННЫЕ ДАННЫЕ")
print("="*80)
for line in combined_lines:
    print(line)
