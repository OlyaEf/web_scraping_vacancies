from abc import ABC, abstractmethod


class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, keyword, count):
        pass

    @abstractmethod
    def process_vacancies(self, data):
        pass


