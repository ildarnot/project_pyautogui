import time
import pyautogui
import pyperclip
from datetime import datetime
import os
import re

# Задаём текущее время
current_datetime = datetime.now()
custom_format_datetime = current_datetime.strftime("%d.%m.%Y_%H.%M")
txt_file_path = '3 ряд_1262G3_output_2025.11.17_15.43.txt'
# csv_file_path = '2 ряд_1262G3_2025.11.04_15.25.csv'
# Базовое имя файла без пути и расширения
base_filename = os.path.splitext(os.path.basename(txt_file_path))[0]



# Функция для поиска ячеек с ключевым значением и внос их в программу
def find_value_by_keyword_from_txt(txt_file_path, keyword, wheel=1):
    """
    Находит значение по ключевому слову в TXT‑файле.
    
    Параметры:
    - txt_file_path: путь к TXT‑файлу
    - keyword: искомое ключевое слово (например, '[mn]')
    - wheel: номер колеса (1 или 2); если значение одно — возвращается оно
    
    Возвращает:
    - Значение (строка) или None, если не найдено
    """
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        # Ищем строку, содержащую ключевое слово
        if keyword in line:
            # Извлекаем часть после закрывающей скобки ']'
            after_bracket = line.split(']', 1)  # Разбиваем по первой ']'
            if len(after_bracket) < 2:
                continue  # Нет данных после ']'
            
            data_part = after_bracket[1].strip()

            # Ищем все числа (целые и дробные, с минусом)
            numbers = re.findall(r'-?\d+\.?\d*', data_part)
            if not numbers:
                return None

            # Возвращаем нужное значение по номеру колеса
            if len(numbers) == 1:
                return numbers[0]
            elif len(numbers) >= 2:
                return numbers[wheel - 1]  # wheel=1 → index 0, wheel=2 → index 1

    return None  # Ключевое слово не найдено

# Входные параметры (пример для Колеса 1)
mn = find_value_by_keyword_from_txt(txt_file_path, '[mn]', wheel=1)
z = find_value_by_keyword_from_txt(txt_file_path, '[z]', wheel=1)
beta = find_value_by_keyword_from_txt(txt_file_path, '[β]', wheel=1)
x_rack = find_value_by_keyword_from_txt(txt_file_path, 'Данные для финишной обработки [x]', wheel=1)
b = find_value_by_keyword_from_txt(txt_file_path, '[b]', wheel=1)
alpha_n = find_value_by_keyword_from_txt(txt_file_path, '[αn]', wheel=1)
haP = find_value_by_keyword_from_txt(txt_file_path, '[haP*]', wheel=1)
hfP = find_value_by_keyword_from_txt(txt_file_path, '[hfP*]', wheel=1)
rho_fP = find_value_by_keyword_from_txt(txt_file_path, '[ρfP*]', wheel=1)
hprP = find_value_by_keyword_from_txt(txt_file_path, 'Коэффициент высоты протуберанца [hprP*]', wheel=1)
alpha_prP = find_value_by_keyword_from_txt(txt_file_path, '[αprP]', wheel=1)


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


# # Количестов знаков после запятой
# x, y=pyautogui.locateCenterOnScreen("decimals_button.png", confidence=0.8)
# pyautogui.click(x, y, 1, 0.1)
# pyautogui.click(x+200, y, 3, 0.1)
# decimals=4
# pyautogui.typewrite(str(decimals))

# Нажатие на модуль и вписывание другого значения
x, y = pyautogui.locateCenterOnScreen("module_button.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
pyautogui.typewrite(str(mn))

# Количество зубьев
x, y = pyautogui.locateCenterOnScreen("teeth_number_button.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
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
pyautogui.typewrite(str(beta))

# Выбор смещения X
x, y = pyautogui.locateCenterOnScreen("X_button.png", confidence=0.7)
pyautogui.click(x+100, y-25, 3, 0.1)
pyautogui.typewrite(str(x_rack))

# Поиск изображения и левой верхней точки "Ширина венца"
x, y = pyautogui.locateCenterOnScreen("window2.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
pyautogui.typewrite(str(b))

# Выбор Профиля рейки
x, y = pyautogui.locateCenterOnScreen("rack_prfl_button.png", confidence=0.7)
pyautogui.click(x, y)

# Выбор угла альфа
x, y = pyautogui.locateCenterOnScreen("degree_alfa_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
pyautogui.typewrite(str(alpha_n))

# Выбор ha коэффициента высоты головки зуба
x, y = pyautogui.locateCenterOnScreen("ha_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
pyautogui.typewrite(str(haP))

# Выбор hf коэффициента высоты ножки зуба
x, y = pyautogui.locateCenterOnScreen("hf_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
pyautogui.typewrite(str(hfP))

# Выбор r коэффициента радиуса переходной кривой
x, y = pyautogui.locateCenterOnScreen("r_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
pyautogui.typewrite(str(rho_fP))


# Выбор галочки на протуберанце
x, y = pyautogui.locateCenterOnScreen("protub_button.png", confidence=0.7)
pyautogui.click(x+110, y, 1, 0.2)

# Выбор hpr
x, y = pyautogui.locateCenterOnScreen("hpr_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
pyautogui.typewrite(str(hprP))

# Выбор alfa_pr
x, y = pyautogui.locateCenterOnScreen("degree_alfa_pr_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
pyautogui.typewrite(str(alpha_prP))

# Нажатие на кнопку произвести расчёт
calc=pyautogui.locateCenterOnScreen("calc_button.png", confidence=0.7)
pyautogui.click(calc)

# Ожидание пока не отобразится всё на экране
time.sleep(0.5)

# # Нажатие на кнопку сохранить в эксель
# excel_exp=pyautogui.locateCenterOnScreen("excel_exp_button.png", confidence=0.8)
# pyautogui.click(excel_exp)

# Нажатие на кнопку сохранить в эксель
txt_exp=pyautogui.locateCenterOnScreen("txt_exp_button.png", confidence=0.8)
pyautogui.click(txt_exp)

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
# Копируем в буфер
pyperclip.copy(base_filename)
pyautogui.click(x, y)
# Вставляем текст
pyautogui.hotkey('ctrl', 'v')

# Нажатие на кнопку сохранить
save=pyautogui.locateCenterOnScreen("save_button.png", confidence=0.7)
pyautogui.click(save)