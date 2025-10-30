import time
import pyautogui

pyautogui.PAUSE = 2
pyautogui.FAILSAFE=True

# Нажатие на кнопку запуска программы
pyautogui.click(3709, 79)

# Нажатие на кнопку Расчёт шестерни
pyautogui.PAUSE = 6
pyautogui.click(1908, 1000)

# Нажатие на кнопку произвести расчёт
pyautogui.PAUSE = 1
pyautogui.click(2471, 1556)

# Нажатие на модуль и вписывание другого значения
# pyautogui.PAUSE = 1
pyautogui.click(1432, 447, 3, 0.1)
# pyautogui.hotkey('ctrl', 'a')
# pyautogui.press('backspace'*5)
pyautogui.typewrite("7")

# Нажатие на кнопку произвести расчёт
# pyautogui.PAUSE = 1
pyautogui.click(2471, 1556)