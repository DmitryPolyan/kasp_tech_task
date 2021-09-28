import os.path
import gzip
from typing import List, TextIO


class FileTypeNotSupported(Exception):
    pass


def parse_file(path: str) -> List[dict]:
    """
    :param path: Путь до исходного текстового файла
    :return: список словарей
    """
    if not os.path.exists(path):
        raise FileNotFoundError
    if path.endswith('.gz'):
        with gzip.open(path, 'rt', encoding='utf-8') as file:
            return dicts_maker(file)
    elif path.endswith('.txt'):
        with open(path, 'r') as file:
            return dicts_maker(file)
    else:
        raise FileTypeNotSupported


def dicts_maker(file: TextIO) -> List[dict]:
    """
    Создание словарей из документов из файла
    :param file: файл с документами
    :return: Список словарей
    """
    temp_dict = dict()
    dicts = []
    for string in file:
        if string[0] == '#':
            continue
        if string == '\n':
            if len(temp_dict):
                # TODO: Лучше реализовать загрузку словаря сразу в БД, вместо списка dicts при работе с большими файлами
                dicts.append(temp_dict)
                temp_dict = dict()
            continue
        if string[0] != ' ':
            key, value = string.split(':', maxsplit=1)
            if key in temp_dict:
                temp_dict[key] = temp_dict[key] + '\n' + value.lstrip()[:-1]
            else:
                temp_dict[key] = value.lstrip()[:-1]
        else:
            temp_dict[key] = temp_dict[key] + '\n' + string.lstrip()[:-1]
    if temp_dict:
        dicts.append(temp_dict)
    return dicts


def load_data(path: str):
    parsed_data = parse_file(path)

    for document in parsed_data:
        ...
        # load document to database (or do something else)
