import zipfile
from typing import Dict


def unzip_file(data: str) -> None:
    """
    Функция для распаковки архива.

    :param:
        data[str]: наименование книги
    """
    result_unzip = zipfile.ZipFile(data, 'r')
    for element in result_unzip.namelist():
        result_unzip.extract(element)
    result_unzip.close()


def data_sorting(file) -> Dict:
    """
    Функция делает подсчет количество букв и сортирует по убыванию.

    :param:
        file[str]: путь до файла для сортировки.

    """
    analysis_letters = dict()
    for element in file:
        for sub_element in element:
            if sub_element.isalpha():
                if sub_element.lower() not in analysis_letters:
                    analysis_letters[sub_element.lower()] = 0
                analysis_letters[sub_element.lower()] += 1
    analysis_letters = dict(sorted(analysis_letters.items(), reverse=True, key=lambda letter: letter[1]))
    return analysis_letters


file_name = 'voyna-i-mir.zip'
unzip_file(file_name)
with open('voyna-i-mir.txt', 'r', encoding='utf-8') as path_to_voyna_i_mir:
    analysis_result = (data_sorting(path_to_voyna_i_mir))

for key, value in analysis_result.items():
    print(key, ':', value)