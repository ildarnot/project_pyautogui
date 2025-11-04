import time
import pyautogui
import openpyxl
from datetime import datetime
# import pyscreeze

# Открываем книгу Excel
wb = openpyxl.load_workbook('updated_input_data 31.10.2025.xlsx')
sheet = wb.active  # Или укажите название листа, если нужно

# Задаём текущее время
current_datetime = datetime.now()
custom_format_datetime = current_datetime.strftime("%d.%m.%Y_%H.%M")

# Находим значения по кодовым словам



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
# Читаем значение из ячейки B3
value_from_excel = sheet['B1'].value
pyautogui.typewrite(str(value_from_excel))

# Количество зубьев
x, y = pyautogui.locateCenterOnScreen("teeth_number_button.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
value_from_excel = sheet['B2'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор направления
x, y = pyautogui.locateCenterOnScreen("direction_button.png", confidence=0.7)
pyautogui.click(x+150, y)
time.sleep(0.2)
x, y = pyautogui.locateCenterOnScreen("right_direction_button.png", confidence=0.7)
pyautogui.click(x, y)

# Выбор угла бэта
x, y = pyautogui.locateCenterOnScreen("degree_betta_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B4'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор смещения X
x, y = pyautogui.locateCenterOnScreen("X_button.png", confidence=0.7)
pyautogui.click(x+100, y-25, 3, 0.1)
value_from_excel = sheet['B5'].value
pyautogui.typewrite(str(value_from_excel))

# Поиск изображения и левой верхней точки "Ширина венца"
x, y = pyautogui.locateCenterOnScreen("window2.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
value_from_excel = sheet['B6'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор Профиля рейки
x, y = pyautogui.locateCenterOnScreen("rack_prfl_button.png", confidence=0.7)
pyautogui.click(x, y)

# Выбор угла альфа
x, y = pyautogui.locateCenterOnScreen("degree_alfa_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B7'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор ha коэффициента высоты головки зуба
x, y = pyautogui.locateCenterOnScreen("ha_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B8'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор hf коэффициента высоты ножки зуба
x, y = pyautogui.locateCenterOnScreen("hf_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B9'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор r коэффициента радиуса переходной кривой
x, y = pyautogui.locateCenterOnScreen("r_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B10'].value
pyautogui.typewrite(str(value_from_excel))


# Выбор галочки на протуберанце
x, y = pyautogui.locateCenterOnScreen("protub_button.png", confidence=0.7)
pyautogui.click(x+110, y)

# Выбор hpr
x, y = pyautogui.locateCenterOnScreen("hpr_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B11'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор alfa_pr
x, y = pyautogui.locateCenterOnScreen("degree_alfa_pr_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B12'].value
pyautogui.typewrite(str(value_from_excel))

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