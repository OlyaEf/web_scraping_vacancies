import requests

from src.vacancies_process import VacancyProcessor
from src.vacancy_api import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    def __init__(self):
        self.base_url = 'https://api.hh.ru/'
        self.headers = {
            'User-Agent': 'user_agent_hh',
        }

    def get_vacancies(self, keyword, count):
        if count > 100:
            pages = int(count / 10) + 1
        else:
            pages = int(1)
        endpoint = 'vacancies?text='
        url = f'{self.base_url}{endpoint}'
        params = {
            'keyword': keyword,
            'page': 0,
            'per_page': count
        }
        response = []
        for page in range(pages):
            params.update({'page': page})
            data = requests.get(url, params=params, headers=self.headers)
            response += data.json()['items']
        return response

    def process_vacancies(self, data):
        vacancies = [
            VacancyProcessor(
                name=item['name'],
                salary=item['salary']['to'] if item['salary'] else None,
                description=item['snippet']['responsibility'],
                link=item['alternate_url']
            )
            for item in data
        ]
        return vacancies
