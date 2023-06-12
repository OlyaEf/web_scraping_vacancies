import os

import requests

from src.vacancies_process import VacancyProcessor
from src.vacancy_api import VacancyAPI


class SuperJobAPI(VacancyAPI):
    superjob_api_key = os.environ.get('superjob_api_key')

    def __init__(self):
        self.base_url = 'https://api.superjob.ru/2.0/'
        self.headers = {
            'X-Api-App-Id': self.superjob_api_key,
        }

    def get_vacancies(self, keyword, count):
        if count > 100:
            pages = int(count / 10) + 1
        else:
            pages = int(1)
        endpoint = 'vacancies/?keyword='
        url = f'{self.base_url}{endpoint}'
        params = {
            'keyword': keyword,
            'page': 0,
            'count': count
        }
        response = []
        for page in range(pages):
            params.update({'page': page})
            data = requests.get(url, params=params, headers=self.headers)
            response += data.json()['objects']
        return response

    def process_vacancies(self, data):
        vacancies = [
            VacancyProcessor(
                name=item['profession'],
                salary=item['payment_from'],
                description=item['client'].get('description'),
                link=item['link']
            )
            for item in data
        ]
        return vacancies
