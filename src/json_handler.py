import json
import os
from abc import abstractmethod, ABC
from typing import List

from src.vacancies_process import VacancyProcessor


class Handler(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: VacancyProcessor) -> None:
        pass

    @abstractmethod
    def get_vacancy(self, keyword: str) -> List[VacancyProcessor]:
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy: VacancyProcessor) -> None:
        pass


class JSONHandler(Handler):
    def __init__(self, filename):
        self.__filename = filename
        if not os.path.isfile(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    @property
    def file(self):
        return self.__filename

    @file.setter
    def file(self, name):
        self.__filename = name

    def add_vacancy(self, vacancy: VacancyProcessor) -> None:
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
        except FileNotFoundError:
            file_data = []
        file_data.append(vacancy.__dict__)  # Преобразование вакансии в словарь
        with open(self.__filename, 'w', encoding='utf') as f:
            json.dump(file_data, f, indent=4, ensure_ascii=False)

    def get_vacancy(self, keyword: str) -> List[VacancyProcessor]:
        found_vacancies = []
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
        except FileNotFoundError:
            return []
        for item in file_data:
            if keyword.lower() in item['name'].lower():
                found_vacancies.append(item)
        return found_vacancies

    def remove_vacancy(self, vacancy: VacancyProcessor) -> None:
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                file_name = json.load(f)
        except FileNotFoundError:
            return
        updated_data = [item for item in file_name if item['name'].lower() != vacancy.name.lower()]
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(updated_data, f, indent=4, ensure_ascii=False)
