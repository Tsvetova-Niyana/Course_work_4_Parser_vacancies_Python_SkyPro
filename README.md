## Курсовой проект - “Парсер вакансий”

Среда разработки - PyCharm 2022.1.3 (Community Editor).

Язык разработки - Python3.11.

Разработка представляет собой консольное приложение.
Поддерживает следующие функции:
1. Получение списка вакансий по указанному ключевому слову с выбранной платформы поиска (hh.ru, SuperJob.ru).
2. Сохранение полученного списка вакансий в файл json-формата.
3. Вывод списка ваканчий на экран.
4. Поиск вакансий в списке по указанному размеру зарплаты.
5. Удаление вакансии из файла списка.
6. Вывод топ вакансий по зарплате. Количество вакансий для вывода указывается пользователем.
7. Вывод списка вакансий в отсортированном по определенному параметру виде. Пользователь може задать сортировку по следующим критериям: код вакансии, наименование компании, наименование вакансии, зарплата.
8. Поиск вакансии по ключевому слову. Поиск ключевого слова осуществляется по требованиям вакансии.

На данный момент запуск приложения осуществляется из IDE разработки. После старта работы в консоли пользователю выводятся вопросы. В квадратных скобках рядом с вопросами приведены варианты возможных ответов. Пользователю необходимо выбрать один из вариантов ответов на вопрос, чтобы использовать приведенные выше функции.

## Задание

Напишите программу, которая будет получать информацию о вакансиях с разных платформ в России, сохранять ее в файл и 
позволять удобно работать с ней (добавлять, фильтровать, удалять).

## Требования к реализации

1. Создать абстрактный класс для работы с API сайтов с вакансиями. Реализовать классы, наследующиеся от абстрактного 
класса, для работы с конкретными платформами. Классы должны уметь подключаться к API и получать вакансии.
2. Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название 
вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т.п. (не менее четырех) 
Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, 
которыми инициализируются его атрибуты.
3. Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения 
данных из файла по указанным критериям и удаления информации о вакансиях. Создать класс для сохранения информации о 
вакансиях в JSON-файл. Дополнительно, по желанию, можно реализовать классы для работы с другими форматами, например с 
CSV- или Excel-файлом, с TXT-файлом.
4. Создать функцию для взаимодействия с пользователем. Функция должна взаимодействовать с пользователем через консоль. 
Самостоятельно придумать сценарии и возможности взаимодействия с пользователем. Например, позволять пользователю 
указать, с каких платформ он хочет получить вакансии, ввести поисковый запрос, получить топ N вакансий по зарплате, 
получить вакансии в отсортированном виде, получить вакансии, в описании которых есть определенные ключевые слова, 
например "postgres" и т.п.
5. Объединить все классы и функции в единую программу.

## Требования к реализации в парадигме ООП

1. Абстрактный класс и классы для работы с API сайтов с вакансиями должны быть реализованы в соответствии 
с принципом наследования.
2. Класс для работы с вакансиями должен быть реализован в соответствии с принципом инкапсуляции и поддерживать методы 
сравнения вакансий между собой по зарплате.
3. Классы и другие сущности в проекте должны удовлетворять минимум первым двум требованиям принципов SOLID.

## Платформы для сбора вакансий

1. **hh.ru** ([ссылка на API](https://github.com/hhru/api/blob/master/docs/general.md))
2. **superjob.ru** ([ссылка на API](https://api.superjob.ru/))
    - Прежде чем начать использовать API от SuperJob, необходимо 
   [зарегистрироваться](https://www.superjob.ru/auth/login/?returnUrl=https://api.superjob.ru/register/) и 
   получить токен для работы. Подробная инструкция дается по ссылке описания документации в разделе 
   [Getting started](https://api.superjob.ru/#gettin). При регистрации приложения можно указать произвольные данные.

## Выходные данные

- Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
- Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.

## Пример использования

Данный пример можно использовать как подсказку к началу реализации. Итоговая реализация может иметь любое количество 
классов, функций и их названий, другой принцип организации.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacancies("Python")
    superjob_vacancies = superjob_api.get_vacancies("Python")

    # Создание экземпляра класса для работы с вакансиями
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
    json_saver.delete_vacancy(vacancy)

    # Функция для взаимодействия с пользователем

    def user_interaction():

        platforms = ["HeadHunter", "SuperJob"]
        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)

        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
            return

        sorted_vacancies = sort_vacancies(filtered_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)


    if __name__ == "__main__":
        user_interaction()
