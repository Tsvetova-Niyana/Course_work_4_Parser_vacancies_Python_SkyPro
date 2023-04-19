"""
Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных
из файла по указанным критериям и удаления информации о вакансиях. Создать класс для сохранения информации о вакансиях
в JSON-файл. Дополнительно, по желанию, можно реализовать классы для работы с другими форматами, например с CSV- или
Excel-файлом, с TXT-файлом.
"""
import json


class JSONSaver:
    """Класс для работы с файлами в json формате"""

    def __init__(self, file_name=None):
        self.__data_file = file_name

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.data_file = value

    def add_vacancy(self, data):
        """Запись выбранных вакансий в файл json"""
        with open(self.data_file, 'w+', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_vacancies_by_salary(self, salary):
        """
        Выбор вакансий по зарплате
        """

        with open(self.data_file, encoding='utf8') as file:
            data = json.load(file)

        res = []
        for item in data:
            if item["salary"] == salary:
                print(json.dumps(item, indent=4, ensure_ascii=False))
                res.append(item)

        return res

    def delete_vacancy(self, query):
        """
        Удаление указанной вакансии из файла
        """

        with open(self.data_file, encoding='utf-8') as file:
            data = json.load(file)

            res = []
            for item in data:
                if int(item['id_vacancy']) == int(query.id):
                    continue
                else:
                    res.append(item)

                    with open(self.data_file, 'w+', encoding='utf8') as file:
                        json.dump(res, file, ensure_ascii=False, indent=4)
