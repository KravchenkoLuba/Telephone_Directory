# Модуль осуществляет все фукнкции работы с БД
def m_adding(name_path_file : str, record : list) -> int:
    '''
    функия для добавления записи(-ей) в конец БД (файла .json)
    Аргументы:
        name_path_file  - тип данных "str | строка"
                        в данной реализации имя файла БД с расширением .json
                        без указания пути к файлу (корневой каталог с файлом main.py)
        record - тип данных "list | список"
                список из словарей: 1 запись|строка в БД или несколько записей|строк в БД
                                    [dict(i)], где i от 1 до len+1
    Значение:
        1 - штатное выполнение
        -1 - сбой при выполнении, для отправки сообщения из контроллера в ui
    Пояснение:
        1. Поверка передали 1 запись в БД или несколько записей в БД (сколько словарей в списке)
        2. Преобразование в .json
        3. Окрытие файла для добавления и запись в конец
    '''
    try:
        import json                                 # импортируем библиотеку
        with open(name_path_file, "a+", encoding='utf-8') as my_file:  # Записываем в файл
            for i in range(0, len(record)):
                string_json = json.dumps(record[i]) # сериализуем его в JSON-структуру, как строку
                # print(string_json)
                my_file.write(f'{string_json}\r')  # Записываем в файл с возвратом корретки
        return 1
    except:
        return -1

def m_delete(name_path_file : str, id_value : int) -> int:
    '''
    функия удаления записи указанной позиции в БД (файла .json)
    Аргументы:
        name_path_file  - тип данных "str | строка"
                        в данной реализации имя файла БД с расширением .json
                        без указания пути к файлу (корневой каталог с файлом main.py)
        id_value - тип данных список из "int"
                    номер или id-записи для удаления из БД

    Значение:
        1 - штатное выполнение
        -1 - сбой при выполнении, для отправки сообщения из контроллера в ui
    Пояснение:
        1. Окрытие файла на чтение .json
        2. Сохранение в типе данных json
        3. Закрытие файла .json
        4. Удаление строки с нужным номером id
        5. Открытие файла перезапись .json
        6. Перезапись файла в типе данных json
        3. Закрытие файла
    '''
    # try:
    #     import json                                 # импортируем библиотеку
    #     with open(name_path_file, "r", encoding='utf-8') as my_file:  # Записываем в файл
    #         string_json = my_file.readlines()
    # #     string_json 

    #     for i in range(0, len(record)):
    #         string_json = json.dumps(record[i]) # сериализуем его в JSON-структуру, как строку
    #         # print(string_json)
    #         my_file.write(f'{string_json}\r')  # Записываем в файл с возвратом корретки
    #     return 1
    # except:
    #     return -1

def m_edit(name_path_file : str, id_value : int) -> int:
    '''
    функия редактирования записи указанной позиции в БД (файла .json)
    Аргументы:
        name_path_file  - тип данных "str | строка"
                        в данной реализации имя файла БД с расширением .json
                        без указания пути к файлу (корневой каталог с файлом main.py)
        id_value - тип данных список из "int"
                    номер или id-записи для редактирования из БД

    Значение:
        1 - штатное выполнение
        -1 - сбой при выполнении, для отправки сообщения из контроллера в ui
    Пояснение:
        1. Окрытие файла на чтение .json
        2. Сохранение в типе данных json
        3. Закрытие файла .json
        4. Замена строки с нужным номером id
        5. Открытие файла перезапись .json
        6. Перезапись файла в типе данных json
        3. Закрытие файла
    '''
    pass

def m_search(name_path_file : str, input_str : str) -> list:
    '''
    функия поиска записи по указанному значению в БД (файла .json)
    Аргументы:
        name_path_file  - тип данных "str | строка"
                        в данной реализации имя файла БД с расширением .json
                        без указания пути к файлу (корневой каталог с файлом main.py)
        input_str - строка (но думаю должен быть правильно сформированный словарь или список)
                    значение для поиска
    Значение:
        result - штатное выполнение возвращается список из словарей
        -1 - сбой при выполнении, возвращается список из [-1]
    Пояснение:
        1. Окрытие файла на чтение .json
        2. Сохранение в типе данных json
        3. Закрытие файла .json
        4. Поиск строк по нужному критерию
        5. Формирование нового словаря из результата поиска
    '''
    pass

# def convert_str_to_dict(t_str : str) -> dict:
#     pass