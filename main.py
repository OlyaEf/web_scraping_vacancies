import os.path

from src.hh import HeadHunterAPI
from src.json_handler import JSONHandler
from src.superjob import SuperJobAPI


def interact_with_user():
    print("Добро пожаловать! Выберите одно из следующих действий:")
    print("1. Получить вакансии с HeadHunter")
    print("2. Получить вакансии с SuperJob")
    print("3. Выйти")

    while True:
        choice = input("Введите номер действия: ")

        if choice == "1":
            keyword = input("Введите поисковый запрос: ")
            n = int(input("Введите количество вакансий: "))

            hh = HeadHunterAPI()
            data_hh = hh.get_vacancies(keyword, n)
            processed_vacancies_hh = hh.process_vacancies(data_hh)

            print(f"Запрошенное количество вакансий с HeadHunter: {len(data_hh)}")
            print("Список вакансий HeadHunter:")
            for item in processed_vacancies_hh:
                print(item)

            file_hh = 'vacancies_hh.json'
            if os.path.isfile(file_hh):
                os.remove(file_hh)
            add_hh = JSONHandler(file_hh)
            for item in processed_vacancies_hh:
                add_hh.add_vacancy(item)

        elif choice == "2":
            keyword = input("Введите поисковый запрос: ")
            n = int(input("Введите количество вакансий: "))

            sj = SuperJobAPI()
            data_sj = sj.get_vacancies(keyword, n)
            processed_vacancies_sj = sj.process_vacancies(data_sj)

            print(f"Запрошенное количество вакансий с SuperJob: {len(data_sj)}")
            print("Список вакансий SuperJob:")
            for item in processed_vacancies_sj:
                print(item)

            file_sj = 'vacancies_sj.json'
            if os.path.isfile(file_sj):
                os.remove(file_sj)
            add_sj = JSONHandler(file_sj)
            for item in processed_vacancies_sj:
                add_sj.add_vacancy(item)

        elif choice == "3":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    interact_with_user()
