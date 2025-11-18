import re

# Выгрузка данных из вводного txt "3 ряд_1262G3_output_2025.11.17_15.43.txt" для первого колеса
def extract_data_gear_1(line):
    pattern = r'^(.*?\])\s+([\d.]+(?:\s*/\s*[\d.]+)?)'
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        value = match.group(2)
        return name, value
    else:
        return None, None

# Примеры использования
print('extract_data_gear_1')
lines = []
with open('3 ряд_1262G3_output_2025.11.17_15.43.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # пропускаем пустые строки
            lines.append(line.strip())

for line in lines:
    name, value = extract_data_gear_1(line)
    print(f"Название: {name}, Значение: {value}")

# Выгрузка данных из вводного txt "3 ряд_1262G3_output_2025.11.17_15.43.txt" для второго колеса
print('extract_data_gear_2')
def extract_data_gear_2(line):
    # Ищем всё от начала строки до ] включительно — это название
    bracket_match = re.search(r'^.*?\]', line)
    if not bracket_match:
        return None, None  # Если скобки ] нет — не обрабатываем
    
    name = bracket_match.group(0)  # Само совпадение (всё до ] включительно)
    
    # Остаток строки после названия
    rest = line[len(name):].strip()
    
    # Находим ВСЕ числовые фрагменты (числа с точкой, возможно разделённые /)
    # Шаблон: число (\d+\.?\d*), затем возможно / и снова число — повторяется
    number_groups = re.findall(r'\d+\.?\d*(?:\s*/\s*\d+\.?\d*)*', rest)
    
    if not number_groups:
        return name, None  # Нет чисел — значение None
    
    # Берём ПОСЛЕДНЮЮ найденную группу чисел
    value = number_groups[-1]
    
    return name, value.strip()

# Примеры использования
lines = []
with open('3 ряд_1262G3_output_2025.11.17_15.43.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # пропускаем пустые строки
            lines.append(line.strip())

for line in lines:
    name, value = extract_data_gear_2(line)
    print(f"Название: {name}, Значение: {value}")

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

print('extract_output_data_gear')
lines = []
failed_lines = []
with open('3 ряд_1262G3_output_2025.11.17_15.43_2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # пропускаем пустые строки
            lines.append(line.strip())

for line in lines:
    name, value = extract_data_gear_output(line)
    print(f"Название: {name}, Значение: {value}")

# Выводим строки, не совпавшие с шаблоном
if failed_lines:
    print("\n--- Строки, не совпавшие с регулярным выражением ---")
    for failed_line in failed_lines:
        print(failed_line)
else:
    print("\n--- Все строки успешно распознаны ---")




# import re
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from typing import Dict, List, Tuple, Optional
# import warnings
# warnings.filterwarnings('ignore')

# class GearAnalysis:
#     def __init__(self):
#         self.input_data = {}
#         self.output_data = {}
#         self.comparison_results = []
    
#     def parse_input_file(self, filepath: str):
#         """Парсинг файла с входными данными"""
#         with open(filepath, 'r', encoding='utf-8') as f:
#             content = f.read()
        
#         # Ищем секцию входных данных по ключевым словам (без жёстких подчёркиваний)
#         input_start = content.find('Список слов, которые требуются для ввода в программу')
#         output_start = content.find('Список выходных данных')
        
#         if input_start == -1:
#             raise ValueError("Не найдена секция входных данных")
#         if output_start == -1:
#             raise ValueError("Не найдена секция выходных данных")
        
#         input_section = content[input_start:output_start]
#         lines = input_section.strip().split('\n')[1:]  # пропускаем заголовок
        

#         for line in lines:
#                 line = line.strip()
#                 if not line:
#                     continue

#                 # Вариант 1: есть единица измерения в скобках
#                 match = re.match(r'(.+?)\s*\((.+?)\)\s*\[(.+?)\]\s*(.+)', line)
#                 if match:
#                     name, unit, code, value = match.groups()
#                     self.input_data[code] = {
#                         'name': name.strip(),
#                         'unit': unit.strip(),
#                         'value': self._parse_values(value),
#                         'source': 'input'
#                     }
#                 else:
#                     # Вариант 2: нет единицы измерения
#                     match = re.match(r'(.+?)\s*\[(.+?)\]\s*(.+)', line)
#                     if match:
#                         name, code, value = match.groups()
#                         self.input_data[code] = {
#                             'name': name.strip(),
#                             'unit': '',
#                             'value': self._parse_values(value),
#                             'source': 'input'
#                         }
#                     else:
#                         print(f"Не удалось разобрать строку: {line}")
    
#     def parse_output_file(self, filepath: str):
#         with open(filepath, 'r', encoding='utf-8') as f:
#             lines = f.readlines()
        
#         for line in lines:
#             line = line.strip()
#             if not line:
#                 continue
            
#             # Разделяем по пробелам/табуляциям (минимум 2 пробела или табуляция)
#             parts = re.split(r'\s{2,}|\t', line)
#             if len(parts) < 2:
#                 continue
            
#             key = parts[0].strip()
#             value = parts[1].strip()
            
#             code_match = re.search(r'\[(.+?)\]', key)
#             if code_match:
#                 code = code_match.group(1)
#                 param_name = key.replace(f'[{code}]', '').strip()
                
#                 self.output_data[code] = {
#                     'name': param_name,
#                     'value': self._parse_single_value(value),
#                     'source': 'output'
#                 }
    
#     def _parse_values(self, value_str: str) -> List[float]:
#         """Преобразует строку значений в список чисел"""
#         return [float(x.strip()) for x in value_str.split() if x.strip()]
    
#     def _parse_single_value(self, value_str: str) -> float:
#         """Преобразует строковое значение в число"""
#         # Удаляем единицы измерения и пояснения
#         value_str = re.sub(r'[^\d\.\-\+]', '', value_str)
#         return float(value_str) if value_str else 0.0
    
#     def compare_data(self, tolerance: float = 0.01) -> pd.DataFrame:
#         """
#         Сравнение входных и выходных данных
#         tolerance - допустимое относительное отклонение (по умолчанию 1%)
#         """
#         results = []
        
#         for code, input_item in self.input_data.items():
#             if code in self.output_data:
#                 output_item = self.output_data[code]
                
#                 input_vals = input_item['value']
#                 output_val = output_item['value']
                
#                 # Сравниваем каждое значение из входных данных с выходным
#                 for i, input_val in enumerate(input_vals):
#                     diff = output_val - input_val
#                     rel_diff = abs(diff / input_val) if input_val != 0 else abs(diff)
                    
#                     is_match = rel_diff <= tolerance
                    
#                     results.append({
#                         'Код': code,
#                         'Название': input_item['name'],
#                         'Единица': input_item['unit'],
#                         'Входное_значение': input_val,
#                         'Выходное_значение': output_val,
#                         'Разница': diff,
#                         'Отклонение_%': rel_diff * 100,
#                         'Соответствие': 'Да' if is_match else 'Нет',
#                         'Порог_отклонения_%': tolerance * 100
#                     })
        
#         self.comparison_results = pd.DataFrame(results)
#         return self.comparison_results
    
#     def generate_report(self, output_csv: str = 'comparison_report.csv'):
#         """Генерация CSV-отчёта"""
#         if self.comparison_results.empty:
#             print("Нет данных для отчёта. Сначала выполните сравнение.")
#             return
        
#         self.comparison_results.to_csv(output_csv, index=False, encoding='utf-8-sig')
#         print(f"Отчёт сохранён в {output_csv}")
    
#     def visualize_results(self):
#         """Визуализация результатов сравнения"""
#         if self.comparison_results.empty:
#             print("Нет данных для визуализации.")
#             return
        
#         # Создаём фигуру с подграфиками
#         fig, axes = plt.subplots(2, 2, figsize=(14, 10))
#         fig.suptitle('Анализ соответствия входных и выходных данных', fontsize=16)
        
#         # 1. Гистограмма отклонений
#         axes[0, 0].hist(self.comparison_results['Отклонение_%'], bins=15, color='skyblue', edgecolor='black')
#         axes[0, 0].set_title('Распределение отклонений (%)')
#         axes[0, 0].set_xlabel('Отклонение (%)')
#         axes[0, 0].set_ylabel('Количество параметров')
#         axes[0, 0].axvline(x=self.comparison_results['Порог_отклонения_%'].iloc[0], 
#                              color='red', linestyle='--', label='Порог')
#         axes[0, 0].legend()
        
#         # 2. Точечная диаграмма: вход vs выход
#         scatter = axes[0, 1].scatter(self.comparison_results['Входное_значение'],
#                                    self.comparison_results['Выходное_значение'],
#                                    c=self.comparison_results['Отклонение_%'],
#                                    cmap='viridis', alpha=0.7)
#         axes[0, 1].set_title('Входные vs Выходные значения')
#         axes[0, 1].set_xlabel('Входное значение')
#         axes[0, 1].set_ylabel('Выходное значение')
#         axes[0, 1].plot([self.comparison_results['Входное_значение'].min(),
#                           self.comparison_results['Входное_значение'].max()],
#                          [self.comparison_results['Входное_значение'].min(),
#                           self.comparison_results['Входное_значение'].max()],
#                          'r--', alpha=0.5, label='Идеальное соответствие')
#         axes[0, 1].legend()
#         plt.colorbar(scatter, ax=axes[0, 1], label='Отклонение (%)')
        
#                 # 3. Столбчатая диаграмма отклонений по параметрам (топ‑10)
#         top_10 = self.comparison_results.nlargest(10, 'Отклонение_%')
#         axes[1, 0].barh(top_10['Код'], top_10['Отклонение_%'], color='salmon')
#         axes[1, 0].set_title('Топ‑10 параметров с наибольшим отклонением (%)')
#         axes[1, 0].set_xlabel('Отклонение (%)')
#         axes[1, 0].set_ylabel('Код параметра')
#         axes[1, 0].invert_yaxis()  # Чтобы самые большие отклонения были вверху

#         # 4. Круговая диаграмма соответствия
#         match_counts = self.comparison_results['Соответствие'].value_counts()
#         axes[1, 1].pie(match_counts.values, labels=match_counts.index, autopct='%1.1f%%',
#                         colors=['#66b3ff', '#ff9999'])
#         axes[1, 1].set_title('Доля параметров по соответствию')

#         plt.tight_layout()
#         plt.show()

#     def summary_statistics(self) -> Dict:
#         """Вычисление сводной статистики"""
#         if self.comparison_results.empty:
#             return {}

#         return {
#             'Общее_количество_параметров': len(self.comparison_results),
#             'Количество_соответствующих': (self.comparison_results['Соответствие'] == 'Да').sum(),
#             'Количество_несоответствующих': (self.comparison_results['Соответствие'] == 'Нет').sum(),
#             'Среднее_отклонение_%': self.comparison_results['Отклонение_%'].mean(),
#             'Максимальное_отклонение_%': self.comparison_results['Отклонение_%'].max(),
#             'Минимальный_отклонение_%': self.comparison_results['Отклонение_%'].min(),
#             'Стандартное_отклонение_%': self.comparison_results['Отклонение_%'].std()
#         }

#     def print_summary(self):
#         """Печать сводной информации"""
#         stats = self.summary_statistics()
#         if not stats:
#             print("Нет данных для сводки.")
#             return

#         # print("\n! + "="*50)
#         print("\n" + "="*50)
#         print("СВОДНАЯ СТАТИСТИКА СРАВНЕНИЯ")
#         print("="*50)
#         for key, value in stats.items():
#             if isinstance(value, float):
#                 print(f"{key}: {value:.3f}")
#             else:
#                 print(f"{key}: {value}")
#         print("="*50)

#     def get_mismatched_parameters(self) -> pd.DataFrame:
#         """Возвращает только параметры с несоответствиями"""
#         return self.comparison_results[self.comparison_results['Соответствие'] == 'Нет']

#     def export_mismatches(self, filepath: str):
#         """Экспорт параметров с несоответствиями в CSV"""
#         mismatches = self.get_mismatched_parameters()
#         if not mismatches.empty:
#             mismatches.to_csv(filepath, index=False, encoding='utf-8-sig')
#             print(f"Параметры с несоответствиями сохранены в {filepath}")
#         else:
#             print("Нет параметров с несоответствиями для экспорта.")



# # " Пример использования
# def main():
#     # Создаём анализатор
#     analyzer = GearAnalysis()

#     # Парсим файлы (укажите актуальные пути)
#     analyzer.parse_input_file('3 ряд_1262G3_output_2025.11.17_15.43.txt')
#     analyzer.parse_output_file('3 ряд_1262G3_output_2025.11.17_15.43_2.txt')

#     # Сравниваем данные (порог отклонения 1%)
#     results = analyzer.compare_data(tolerance=0.01)

#     # Выводим сводную статистику
#     analyzer.print_summary()

#     # Показываем параметры с несоответствиями
#     mismatches = analyzer.get_mismatched_parameters()
#     if not mismatches.empty:
#         print("\nПАРАМЕТРЫ С НЕСООТВЕТСТВИЯМИ:")
#         print(mismatches[['Код', 'Название', 'Входное_значение',
#                        'Выходное_значение', 'Отклонение_%']])

#     # Генерируем отчёт
#     analyzer.generate_report('comparison_report.csv')

#     # Визуализируем результаты
#     analyzer.visualize_results()

#     # Экспортируем только несоответствия
#     analyzer.export_mismatches('mismatches_report.csv')



# if __name__ == '__main__':
#     main()
