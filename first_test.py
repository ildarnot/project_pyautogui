import time
import pyautogui
import openpyxl
# import pyscreeze

# Открываем книгу Excel
wb = openpyxl.load_workbook('input_data.xlsx')
sheet = wb.active  # Или укажите название листа, если нужно

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

# Нажатие на кнопку произвести расчёт
pyautogui.click(2471, 1556)

# Очистка графиков
clear=pyautogui.locateCenterOnScreen("clear_button.png", confidence=0.7)
pyautogui.click(clear)

# Нажатие на модуль и вписывание другого значения
x, y = pyautogui.locateCenterOnScreen("module_button.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
# Читаем значение из ячейки B3
value_from_excel = sheet['B3'].value
pyautogui.typewrite(str(value_from_excel))

# Количество зубьев
x, y = pyautogui.locateCenterOnScreen("teeth_number_button.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
value_from_excel = sheet['B4'].value
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
value_from_excel = sheet['B6'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор смещения X
x, y = pyautogui.locateCenterOnScreen("X_button.png", confidence=0.7)
pyautogui.click(x+100, y-25, 3, 0.1)
value_from_excel = sheet['B8'].value
pyautogui.typewrite(str(value_from_excel))

# Поиск изображения и левой верхней точки "Ширина венца"
x, y = pyautogui.locateCenterOnScreen("window2.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
value_from_excel = sheet['B10'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор Профиля рейки
x, y = pyautogui.locateCenterOnScreen("rack_prfl_button.png", confidence=0.7)
pyautogui.click(x, y)

# Выбор угла альфа
x, y = pyautogui.locateCenterOnScreen("degree_alfa_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B12'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор ha коэффициента высоты головки зуба
x, y = pyautogui.locateCenterOnScreen("ha_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B13'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор hf коэффициента высоты ножки зуба
x, y = pyautogui.locateCenterOnScreen("hf_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B14'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор r коэффициента радиуса переходной кривой
x, y = pyautogui.locateCenterOnScreen("r_button.png", confidence=0.7)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B15'].value
pyautogui.typewrite(str(value_from_excel))


# Выбор галочки на протуберанце
x, y = pyautogui.locateCenterOnScreen("protub_button.png", confidence=0.7)
pyautogui.click(x+110, y)

# Выбор hpr
x, y = pyautogui.locateCenterOnScreen("hpr_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B16'].value
pyautogui.typewrite(str(value_from_excel))

# Выбор alfa_pr
x, y = pyautogui.locateCenterOnScreen("degree_alfa_pr_button.png", confidence=0.8)
pyautogui.click(x+100, y, 3, 0.1)
value_from_excel = sheet['B17'].value
pyautogui.typewrite(str(value_from_excel))

# Нажатие на кнопку произвести расчёт
calc=pyautogui.locateCenterOnScreen("calc_button.png", confidence=0.7)
pyautogui.click(calc)

# Построение графика с помощью 