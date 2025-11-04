import time
import pyautogui
import openpyxl
from datetime import datetime
import csv
# import pyscreeze

# Открываем книгу Excel
wb = openpyxl.load_workbook('updated_input_data 31.10.2025.xlsx')
sheet = wb.active  # Или укажите название листа, если нужно

# Задаём текущее время
current_datetime = datetime.now()
custom_format_datetime = current_datetime.strftime("%d.%m.%Y_%H.%M")
csv_file_path = '1_row_1262G3_2025.11.04_10.34.csv'


# Функция для поиска ячеек с ключевым значением и внос их в программу
def find_value_by_keyword(csv_file_path, keyword, occurrence=1):
    """
    Находит значение по ключевому слову в CSV.
    
    Параметры:
    - csv_file_path: путь к CSV-файлу
    - keyword: искомое ключевое слово
    - occurrence: номер вхождения (1 = первое, 2 = второе, 3 = третье и т.д.)
    
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



# Описываем паузы между кажддым действием в 0,1 сек
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE=True

# Нажатие на кнопку запуска программы
pyautogui.click(3709, 79)

# Ожидание пока я открою полноэкранный режим
time.sleep(2)

# Нажатие на кнопку Расчёт шестерни
# pyautogui.click(1908, 1000)
window1=pyautogui.locateCenterOnScreen("window.png", confidence=0.7)
pyautogui.click(window1)

# Ожидание пока не отобразится всё на экране
time.sleep(0.5)

# # Нажатие на кнопку произвести расчёт
# pyautogui.click(2471, 1556)

# Очистка графиков
clear=pyautogui.locateCenterOnScreen("clear_button.png", confidence=0.7)
pyautogui.click(clear)

# Нажатие на модуль и вписывание другого значения
x, y = pyautogui.locateCenterOnScreen("module_button.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
# # Читаем значение из ячейки B3
# value_from_excel = sheet['B1'].value

# Используем функцию
keyword = '[mn]'
mn = find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(mn))

# Количество зубьев
x, y = pyautogui.locateCenterOnScreen("teeth_number_button.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
# value_from_excel = sheet['B2'].value
keyword = '[z]'
z = find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(z))

# Выбор направления
x, y = pyautogui.locateCenterOnScreen("direction_button.png", confidence=0.7)
pyautogui.click(x+150, y)
time.sleep(0.2)
x, y = pyautogui.locateCenterOnScreen("right_direction_button.png", confidence=0.7)
pyautogui.click(x, y)

# Выбор угла бэта
x, y = pyautogui.locateCenterOnScreen("degree_betta_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
# value_from_excel = sheet['B4'].value
keyword = '[β]'
β = find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(β))

# Выбор смещения X
x, y = pyautogui.locateCenterOnScreen("X_button.png", confidence=0.7)
pyautogui.click(x+100, y-25, 3, 0.1)
# value_from_excel = sheet['B5'].value
keyword = 'Данные для финишной обработки [x]'
x = find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(x))

# Поиск изображения и левой верхней точки "Ширина венца"
x, y = pyautogui.locateCenterOnScreen("window2.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
# value_from_excel = sheet['B6'].value
keyword = '[b]'
b = find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(b))

# Выбор Профиля рейки
x, y = pyautogui.locateCenterOnScreen("rack_prfl_button.png", confidence=0.7)
pyautogui.click(x, y)

# Выбор угла альфа
x, y = pyautogui.locateCenterOnScreen("degree_alfa_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
# value_from_excel = sheet['B7'].value
keyword = '[αn]'
αn = find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(αn))

# Выбор ha коэффициента высоты головки зуба
x, y = pyautogui.locateCenterOnScreen("ha_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
# value_from_excel = sheet['B8'].value
keyword = '[haP*]'
ha= find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(ha))

# Выбор hf коэффициента высоты ножки зуба
x, y = pyautogui.locateCenterOnScreen("hf_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
# value_from_excel = sheet['B9'].value
keyword = '[hfP*]'
hf= find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(hf))

# Выбор r коэффициента радиуса переходной кривой
x, y = pyautogui.locateCenterOnScreen("r_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
# value_from_excel = sheet['B10'].value
keyword = '[ρfP*]'
ρf= find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(ρf))


# Выбор галочки на протуберанце
x, y = pyautogui.locateCenterOnScreen("protub_button.png", confidence=0.7)
pyautogui.click(x+110, y)

# Выбор hpr
x, y = pyautogui.locateCenterOnScreen("hpr_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
# value_from_excel = sheet['B11'].value
keyword = 'Коэффициент высоты протуберанца [hprP*]'
hpr = find_value_by_keyword(csv_file_path, keyword, occurrence=3)  # Третий результат
pyautogui.typewrite(str(hpr))

# Выбор alfa_pr
x, y = pyautogui.locateCenterOnScreen("degree_alfa_pr_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
# value_from_excel = sheet['B12'].value
keyword = '[αprP]'
αpr= find_value_by_keyword(csv_file_path, keyword)
pyautogui.typewrite(str(αpr))

# Нажатие на кнопку произвести расчёт
calc=pyautogui.locateCenterOnScreen("calc_button.png", confidence=0.7)
pyautogui.click(calc)

# Ожидание пока не отобразится всё на экране
time.sleep(0.5)

# Нажатие на кнопку сохранить в эксель
excel_exp=pyautogui.locateCenterOnScreen("excel_exp_button.png", confidence=0.8)
pyautogui.click(excel_exp)

# Ожидание пока не отобразится всё на экране
time.sleep(0.5)

# Нажатие на кнопку сохранить тестовая папка
x, y=pyautogui.locateCenterOnScreen("tests_folder.png", confidence=0.7)
pyautogui.click(x, y, 2, 0.1)

# Нажатие на кнопку сохранить результаты из таблицы
x, y=pyautogui.locateCenterOnScreen("table_results_folder.png", confidence=0.7)
pyautogui.click(x, y, 2, 0.1)

# Нажатие на поле Имя файла
x, y=pyautogui.locateCenterOnScreen("file_name.png", confidence=0.7)
pyautogui.click(x, y)
# Значение названия теста
test1 = f'1_row_1262G3_Gear_1_{custom_format_datetime}'
pyautogui.typewrite((test1))

# Нажатие на кнопку сохранить
save=pyautogui.locateCenterOnScreen("save_button.png", confidence=0.7)
pyautogui.click(save)