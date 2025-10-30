import time
import pyautogui
import openpyxl
# import pyscreeze

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

# Нажатие на кнопку произвести расчёт
pyautogui.click(2471, 1556)

# Нажатие на модуль и вписывание другого значения
pyautogui.click(1432, 447, 3, 0.1)
# Открываем книгу Excel
wb = openpyxl.load_workbook('input_data.xlsx')
sheet = wb.active  # Или укажите название листа, если нужно
# Читаем значение из ячейки B3
value_from_excel = sheet['B3'].value
pyautogui.typewrite(str(value_from_excel))

pyautogui.click(1435, 503, 3, 0.1)
pyautogui.typewrite("48")

# Поиск изображения и левой верхней точки "Ширина венца"
x, y = pyautogui.locateCenterOnScreen("window2.png", confidence=0.7)
pyautogui.click(x+150, y, 3, 0.1)
pyautogui.typewrite("50")

# Нажатие на кнопку произвести расчёт
pyautogui.click(2471, 1556)

# Очистка графиков
clear=pyautogui.locateCenterOnScreen("clear_button.png", confidence=0.7)
pyautogui.click(clear)

# Построение графика с помощью 