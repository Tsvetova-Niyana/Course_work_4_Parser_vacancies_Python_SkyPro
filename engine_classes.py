from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass

    def get_vacancies(self):
        pass


class HeadHunterAPI(Engine):
    def get_request(self):
        pass

    def get_vacancies(self):
        pass


class SuperJobAPI(Engine):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_request(self):
        pass

    def get_vacancies(self):
        pass
