"""
Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название вакансии,
ссылка на вакансию, зарплата, краткое описание или требования и т.п. (не менее четырех) Класс должен поддерживать
методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.
"""

class Vacancy:
    """Класс для вакансий"""
    __slots__ = ('id', 'company_name', 'name_vacancy', 'link_to_vacancy', 'requirements', 'remote_work', 'salary')

    def __init__(self, id, company_name=None, name_vacancy=None, link_to_vacancy=None, requirements=None, salary=None):
        self.id = id
        self.company_name = company_name
        self.name_vacancy = name_vacancy
        self.link_to_vacancy = link_to_vacancy
        self.requirements = requirements
        self.salary = salary

    def __repr__(self):
        return f'Наименование вакансии: {self.name_vacancy}\nРаботодатель: {self.company_name}\nСсылка на вакансию:' \
               f' {self.link_to_vacancy}\nОписание вакансии: {self.requirements}\nЗарплата:' \
               f' {self.salary}\n'

    def __str__(self):
        return f'Наименование вакансии: {self.name_vacancy}\nРаботодатель: {self.company_name}\nСсылка на вакансию:' \
               f' {self.link_to_vacancy}\nОписание вакансии: {self.requirements}\nЗарплата:' \
               f' {self.salary}\n'

    def __gt__(self, other):
        return self.salary > other.salary
