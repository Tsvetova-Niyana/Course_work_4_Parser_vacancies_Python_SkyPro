from engine_classes import HeadHunterAPI, SuperJob
from json_saver import JSONSaver
from utils import get_vacancies_by_key_word, print_vacancy, get_vacancies_by_salary, delete_vacancy, top_vacancy, \
    sorted_vac, \
    find_by_keyword


def user_interaction():
    platforms = input("Введите платформу поиска ['HeadHunter', 'SuperJob']: ")
    key_word = input('Введите вакансию для поиска: ').strip()

    if platforms == 'HeadHunter':
        vac_platform = HeadHunterAPI()
        json_saver = JSONSaver('data_list_hh.json')

        # Получаем от пользователя ключевое слово для поиска вакансий
        get_vacancies_by_key_word(vac_platform, json_saver, key_word)

    if platforms == 'SuperJob':
        vac_platform = SuperJob()
        json_saver = JSONSaver('data_list_sj.json')

        # Получаем от пользователя ключевое слово для поиска вакансий
        get_vacancies_by_key_word(vac_platform, json_saver, key_word)

    isprint_vacancy = input("Вывести вакансии ['да', 'нет']: ")
    if isprint_vacancy == 'да':
        # Вывод вакансий на экран из файла
        print_vacancy(json_saver)

    isfind_salary = input("Найти вакансию по зарплате ['да', 'нет']: ")

    if isfind_salary == 'да':
        size_salary = input("Введите размер зарплаты: ")

        # Поиск в файле 'data_list_hh.json' вакансий с указанной зарплатой
        get_vacancies_by_salary(json_saver, size_salary)

    isdel_vacancy = input("Удалить вакансию из файла ['да', 'нет']: ")

    if isdel_vacancy == 'да':
        id_vacancy = input("Введите идентификатор вакансии ('id_vacancy'): ")

        # Удаление из файла вакансии
        delete_vacancy(json_saver, id_vacancy)

    istop_vacancy = input("Показать топ вакансий ['да', 'нет']: ")

    if istop_vacancy == 'да':
        count_top = input("Введите количество вакансий для вывода: ")
        top_vacancy(json_saver, count_top)

    issorted = input("Показать вакансии в отсортированном виде ['да', 'нет']: ")

    if issorted == 'да':
        sorted_by = input("Вывести перечень вакансий по критерию [id_vacancy, company_name, name_vacancy, salary]: ")
        sorted_vac(json_saver, sorted_by)

    isfind = input("Найти вакансии по ключевому слову в описании ['да', 'нет']: ")

    if isfind == 'да':
        keyword = input("Введите ключевое слово поиска: ")
        find_by_keyword(json_saver, keyword)


if __name__ == "__main__":
    user_interaction()
