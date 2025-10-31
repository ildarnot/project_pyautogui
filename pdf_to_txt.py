import pdfplumber

def find_lines_with_word(pdf_path, word):
    lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            # Получаем текст страницы
            text = page.extract_text()
            if text:
                # Разбиваем текст на строки
                for line in text.split('\n'):
                    # Проверяем, присутствует ли искомое слово в строке
                    if word in line:
                        lines.append((page_num + 1, line.strip()))
    return lines

# Пример использования
pdf_file = '1_row_1262G3.pdf'

word_to_find = '[mn]'
lines_found = find_lines_with_word(pdf_file, word_to_find)

word_to_find2 = '[z]'
lines_found2 = find_lines_with_word(pdf_file, word_to_find2)

word_to_find3 = 'Направление наклона'
lines_found3 = find_lines_with_word(pdf_file, word_to_find3)

for page_number, line in lines_found:
    print(f"Слово '{word_to_find}' найдено на странице {page_number}: {line}")

for page_number, line in lines_found2:
    print(f"Слово '{word_to_find2}' найдено на странице {page_number}: {line}")

for page_number, line in lines_found3:
    print(f"Слово '{word_to_find3}' найдено на странице {page_number}: {line}")