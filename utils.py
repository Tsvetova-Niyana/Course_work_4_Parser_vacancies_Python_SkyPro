"""
Функция должна взаимодействовать с пользователем через консоль.
Самостоятельно придумать сценарии и возможности взаимодействия с пользователем.
Например, позволять пользователю указать, с каких платформ он хочет получить вакансии, ввести поисковый запрос,
получить топ N вакансий по зарплате, получить вакансии в отсортированном виде, получить вакансии, в описании которых
есть определенные ключевые слова, например "postgres" и т.п.
"""
import json

from vacancy_classes import Vacancy


def get_vacancies_by_key_word(vac_platform, json_saver, key_word):
    """
    Функция записи вакансий в файл json
    """
    response = vac_platform.get_request(key_word)
    json_saver.add_vacancy(response)


def print_vacancy(json_saver):
    """
    Функция вывода вакансий на экран
    """
    with open(json_saver.data_file, encoding='utf-8') as file:
        data = json.load(file)

        for item in data:
            print(json.dumps(item, indent=4, ensure_ascii=False))


def get_vacancies_by_salary(json_saver, size_salary):
    """
    Функция получения вакансии по указанной зарплате
    """
    res = json_saver.get_vacancies_by_salary(int(size_salary))
    if len(res) == 0:
        print(f"Вакансий с зарплатой {size_salary} р. нет\n")


def delete_vacancy(json_saver, id_vacancy):
    """
    Функция удаления вакансии из файла
    """

    vacancy = Vacancy(id_vacancy)

    # Удаление из файла вакансии
    json_saver.delete_vacancy(vacancy)


def top_vacancy(json_saver, count_top):
    """
    Функция вывода топ вакансий (по зарплатам)
    """

    with open(json_saver.data_file, encoding='utf-8') as file:
        data = json.load(file)

        # Сортировка вакансий по убыванию зарплат с ограничением по количеству вывода
        vac_sorted = sorted(data, key=lambda vac: -vac["salary"])[:int(count_top)]

        for vac in vac_sorted:
            print(json.dumps(vac, indent=4, ensure_ascii=False))


def sorted_vac(json_saver, sorted_by):
    """
     Функция вывода топ вакансий (по зарплатам)
     """

    with open(json_saver.data_file, encoding='utf-8') as file:
        data = json.load(file)

        if sorted_by == 'id_vacancy':
            # Сортировка вакансий по коду вакансии (id_vacancy)
            vac_sorted = sorted(data, key=lambda vac: vac["id_vacancy"])

        if sorted_by == 'company_name':
            # Сортировка вакансий по наименованию компании (company_name)
            vac_sorted = sorted(data, key=lambda vac: vac["company_name"])

        if sorted_by == 'name_vacancy':
            # Сортировка вакансий по наименованию вакансии (name_vacancy)
            vac_sorted = sorted(data, key=lambda vac: vac["name_vacancy"])

        if sorted_by == 'salary':
            # Сортировка вакансий по зарплате (salary)
            vac_sorted = sorted(data, key=lambda vac: vac["salary"])

        for vac in vac_sorted:
            print(json.dumps(vac, indent=4, ensure_ascii=False))


def find_by_keyword(json_saver, keyword):
    """
    Функция поиска вакансии по ключевому слову в требованиях
    """

    with open(json_saver.data_file, encoding='utf-8') as file:

        data = json.load(file)

        for item in data:
            line = item['requirements']

            if line:
                if keyword in line:
                    print(json.dumps(item, indent=4, ensure_ascii=False))
