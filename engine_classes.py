from abc import ABC, abstractmethod

import requests

"""
Создать абстрактный класс для работы с API сайтов с вакансиями. Реализовать классы, наследующиеся от абстрактного 
класса, для работы с конкретными платформами. Классы должны уметь подключаться к API и получать вакансии.
"""
my_api_key: str = 'v3.r.135083517.49eef2199d805e73aa90d5cb1cabb6df87d832f3.cd8d49d02da63b9ca1030c9ba9c41b9af1fc3f1b'


class Engine(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_request(self, keyword):
        """Парсинг сайта по ключевому слову"""
        pass


class HeadHunterAPI(Engine):
    """Класс для получения вакансий с HeadHunter"""

    @staticmethod
    def _get_salary(salary):
        """Обработка поля salary(зарплата):
                - выводит зарплату 'to',
                - в случае отсутствия, выводит зарплату 'from'
                - если оба поля не заполнены выводит 0"""
        if salary:
            if salary.get('to'):
                return salary['to']
            if salary.get('from'):
                return salary['from']
        return 0

    def get_request(self, keyword):
        """Получение вакансий в виде списка"""

        vacancies = []
        for page in range(5):
            response = requests.get(f'https://api.hh.ru/vacancies?text={keyword}',
                                    params={'per_page': 100, 'page': page}).json()
            for vacancy in response['items']:
                vacancies.append({
                    'id_vacancy': f"{vacancy['id']}",
                    'company_name': vacancy['employer']['name'],
                    'name_vacancy': vacancy['name'],
                    'link_to_vacancy': vacancy['alternate_url'],
                    'requirements': vacancy['snippet']['requirement'],
                    'salary': self._get_salary(vacancy.get('salary', {})),
                })
        return vacancies


class SuperJob(Engine):
    """Класс для получения вакансий с SuperJob"""

    @staticmethod
    def _get_salary(salary: dict):
        """Обработка поля salary(зарплата):
                - выводит зарплату 'payment_to',
                - в случае отсутствия, выводит зарплату 'payment_from'
                - если оба поля не заполнены выводит 0"""

        if salary.get('payment_to'):
            return salary['payment_to']
        if salary.get('payment_from'):
            return salary['payment_from']
        return 0

    def get_request(self, keyword):
        """Получение вакансий в виде списка"""

        vacancies = []
        for page in range(5):
            response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers={'X-Api-App-Id': my_api_key},
                                    params={'keywords': keyword, 'count': 100,
                                            'page': page}).json()

            for vacancy in response['objects']:
                vacancies.append({
                    'id_vacancy': vacancy['id'],
                    'company_name': vacancy['firm_name'],
                    'name_vacancy': vacancy['profession'],
                    'link_to_vacancy': vacancy['link'],
                    'requirements': vacancy['candidat'],
                    'salary': self._get_salary(vacancy),
                })
        return vacancies
