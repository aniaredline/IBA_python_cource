import os

# список для строк
line_list = []
# --- чтение файла ---
source_filename = input("Введите имя файла для чтения данных F1:\n")

_, extension = os.path.splitext(source_filename)
if extension == '':
    source_filename += '.txt'

with open(source_filename, "r") as source_file:
    # считываем весь файл как список строк
    content = source_file.readlines()

    str_num_first = int(input("Введите номер первой строки N1:\n"))
    str_num_last = int(input("Введите номер последней строки N2:\n"))
    first_letter = input("Введите первую букву для отбора строк A:\n")

    # цикл по строкам файла
    for index, row in enumerate(content, start=1):
        if str_num_first <= index <= str_num_last and row[0] == first_letter:
            line_list.append(row)

    source_file.close()

# --- запись файла ---

dist_filename = input("Введите имя файла для сохранения данных F2:\n")

_, extension = os.path.splitext(dist_filename)
if extension == '':
    dist_filename += '.txt'

with open(dist_filename, "w") as dist_file:
    # пишем строчки
    dist_file.writelines(line_list)
    dist_file.close()
