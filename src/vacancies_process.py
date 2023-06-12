
class VacancyProcessor:

    def __init__(self, name, salary, description, link):
        self.name = name
        self.salary = salary
        self.description = description
        self.link = link

    def __str__(self):
        return f'вакансия: {self.name}\n' \
               f'оплата: {self.salary}\n' \
               f'описание: {self.description if self.description else "Отсутствует"}\n' \
               f'ссылка: {self.link}\n'

    def __gt__(self, other):
        if isinstance(other, VacancyProcessor):
            return self.salary > other.salary
        raise TypeError('Other is not VacancyProcessor')
