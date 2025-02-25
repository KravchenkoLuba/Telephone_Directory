# Модуль осуществляет все фукнкции работы с БД

def m_adding(name_path_file : str, record : list) -> list or int:
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
        штатное выполнение - возвращает БД в виде списка словарей (для выводав консоль)
        сбой при выполнении - (-1) для отправки сообщения из контроллера в ui
    
    Пояснение:
        1. Передали 1 запись в БД или несколько записей в БД
        2. Преобразование в .json
        3. Окрытие файла для добавления и перезапись
    Примечание!
        В файле читаемом должно быть записано в виде списка с []!
                файл.json:
                [   <-это обязательно!
                    {
                        "id": 1,
                        "surname": "Иванов",
                        "name": "Иван",
                        "fathername": "Иванович",
                        "telefon": 89270010101,
                        "comment": "телефон Иванов"
                    }
                ]  <-это обязательно!
    '''
    try:
        import json                                                     # импортируем библиотеку
        # Действие 1 - считать исходную БД в переменную
        with open(name_path_file, "r", encoding="UTF-8") as my_file:    # читаем из файла
            string_json = my_file.read()
        # Eсли файл пустой
        if string_json == "":                                           
            for i in range(0, len(record)):                             # задаём id c 1 и далее
                (record[i])['id'] = i + 1 
            string_json = json.dumps(record, indent=4, ensure_ascii=False) # десериализация в строку json
            with open(name_path_file, "w", encoding="UTF-8") as my_file:
                my_file.write(string_json)
            return record
        # Иначе если файлне пустой, а уже с имеющимся списком
        list_readed_dicts = json.loads(string_json)                      # проводим десериализацию JSON-объекта
        # Действие 2 - обновление индексов при добавлении
        # Действие 2.1 - поиска последнего индекса в исходной БД
        count_records_in_base_db = len(list_readed_dicts)                # количество записей/строк
        last_dict_in_db = list_readed_dicts[count_records_in_base_db-1]  # ID из последней записи/строки
        id_of_last_dict = last_dict_in_db['id']
        # Действие 2.2 - перезапись id в добавляемой записи(-ей)
        for i in range(0, len(record)):              
            (record[i])['id'] = id_of_last_dict + i + 1                 # приращение id в добавляемых записях  
        # Действие 3 - Добавить данные в конец БД полностью весь новый список
        list_readed_dicts.extend(record)
        # Действие 4 - Перезаписать полностью обновлённую БД c имеющимся обновлением в конце
        string_json = json.dumps(list_readed_dicts, indent=4, ensure_ascii=False) # десериализация в строку json
        with open(name_path_file, "w", encoding="UTF-8") as my_file:
            my_file.write(string_json)
        return list_readed_dicts
    except:
        return -1

def m_delete(name_path_file : str, id_value : int) -> list or int:
    '''
    функия удаления записи указанной позиции в БД (файла .json)
    
    Аргументы:
        name_path_file  - тип данных "str | строка"
                        в данной реализации имя файла БД с расширением .json
                        без указания пути к файлу (корневой каталог с файлом main.py)
        id_value - тип 1 число в "int"
                    номер или id-записи для удаления из БД

    Значение:
        штатное выполнение - возвращает БД в виде списка словарей (для выводав консоль)
        сбой при выполнении - (-1) для отправки сообщения из контроллера в ui
    
    Пояснение:
        1. Окрытие файла на чтение .json
        2. Сохранение в типе данных json
        3. Закрытие файла .json
        4. Удаление строки с нужным номером id
        5. Открытие файла перезапись .json
        6. Перезапись файла в типе данных json
        3. Закрытие файла
    '''
    try:
        import json                                                     # импортируем библиотеку
        # Действие 1 - считать исходную БД в переменную
        with open(name_path_file, "r", encoding="UTF-8") as my_file:    # читаем из файла
            string_json = my_file.read()
        list_readed_dicts = json.loads(string_json)                      # проводим десериализацию JSON-объекта
        # Действие 2 - Удаление по id из списка словарей (БД из файла)
        # Действие 2.1 - Поиск индекса списка по номеру id
        index_of_record_with_needed_id = -1                             # если такого id нет, то удалить не можем
        for i in range(0, len(list_readed_dicts)):                     
            if (list_readed_dicts[i])['id'] == id_value:                # сохранить индекс словаря в списке с нужным id
                index_of_record_with_needed_id = i
                break  # так как id уникальный первичный ключ, одинаковых значений не может быть
        # Действие 2.2 - Непосредственное удаление по найденному индексу (не id)
        if index_of_record_with_needed_id == -1:
            return -1    #если не нашли id в справочнике для удаления, то выходим с отрицательным результатом выполнения
        del(list_readed_dicts[index_of_record_with_needed_id])          # удаление элемента списка по индексу
        # Действие 3 - Перезаписать полностью обновлённую БД с отсутсвием удалённой записи
        string_json = json.dumps(list_readed_dicts, indent=4, ensure_ascii=False) # десериализация в строку json
        with open(name_path_file, "w", encoding="UTF-8") as my_file:
            my_file.write(string_json)
        return list_readed_dicts
    except:
        return -1

def m_edit(name_path_file : str, record : list or dict) ->  list or int:
    '''
    функция редактирования записи по указанному id в БД (файла .json) 
        id и значения для изменения хранятся в словаре/списке

    Аргументы:
        name_path_file  - тип данных "str | строка"
                        в данной реализации имя файла БД с расширением .json
                        без указания пути к файлу (корневой каталог с файлом main.py)
        record_with_changes - список словарей для редактирования, все заполненные значения ключей на перезапись в основную БД
    
    Значение:
        штатное выполнение - возвращает БД в виде списка словарей (для выводав консоль)
        сбой при выполнении - (-1) для отправки сообщения из контроллера в ui

    Пояснение:
        1. Окрытие файла на чтение .json + Сохранение в типе данных json + Закрытие файла .json
        2. Замена строки (словаря в списке) с нужными данными по номеру id, выбранному пользователем и переданным в словаре (списке)
        3. Открытие файла перезапись .json + Перезапись файла в типе данных json +Закрытие файла
    '''
    try:
        import json                                                     # импортируем библиотеку
        # Действие 1 - считать исходную БД в переменную
        with open(name_path_file, "r", encoding="UTF-8") as my_file:    # читаем из файла
            string_json = my_file.read()
        list_readed_dicts = json.loads(string_json)                      # проводим десериализацию JSON-объекта
        # Действие 2 - Редактирование по id из списка словарей (БД из файла)
        # Действие 2.1 - Поиск индекса списка по номеру id
        index_of_record_with_needed_id = -1                             # если такого id нет, то редактировать не можем
        # Если случайно предали искомое как словарь - перезапись его в списк из словарей
        if (type(record) is dict):
            record = [record]
        id_record_to_modify = (record[0])['id']                         # вытащено id из словаря/списка, выбранного пользователем на изменение
        for i in range(0, len(list_readed_dicts)):                      
            if (list_readed_dicts[i])['id'] == id_record_to_modify:                
                index_of_record_with_needed_id = i
                break  # так как id уникальный первичный ключ, одинаковых значений не может быть
        # Действие 2.2 - Непосредственное редактирование по найденномув п. 2.1 индексу (уже не по не id)
        if index_of_record_with_needed_id == -1:
            return -1    #если не нашли id в справочнике для удаления, то выходим с отрицательным результатом выполнения
        i = index_of_record_with_needed_id
        # !!!!Вот это очень нехорошая часть!!!!!
        # так как при изменении сруктуры БД (+- столбец|ключ) всё полетит
        # for key, value in users.items(): print(f"Phone: {key}  User: {value} ")  не даст сразу 2 перебрать
        if (record[0])['surname'] != "":
            (list_readed_dicts[i])['surname'] = (record[0])['surname']
        if (record[0])['name'] != "":
            (list_readed_dicts[i])['name'] = (record[0])['name']
        if (record[0])['fathername'] != "":
            (list_readed_dicts[i])['fathername'] = (record[0])['fathername']
        if (record[0])['telefon'] != 0:
            (list_readed_dicts[i])['telefon'] = (record[0])['telefon']
        if (record[0])['comment'] != "":
            (list_readed_dicts[i])['comment'] = (record[0])['comment']
         # Действие 3 - Перезаписать полностью обновлённую БД с отсутсвием удалённой записи
        string_json = json.dumps(list_readed_dicts, indent=4, ensure_ascii=False) # десериализация в строку json
        with open(name_path_file, "w", encoding="UTF-8") as my_file:
            my_file.write(string_json)
        return list_readed_dicts
    except:
        return -1

def m_search(name_path_file : str, condition_to_find : dict or list) -> list:
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
    test_dict = [
        {
            "id": 1,
            "surname": "Иванов",
            "name": "Иван",
            "fathername": "Иванович",
            "telefon": 89270010101,
            "comment": "телефон Иванов"
        },
        {
            "id": 2,
            "surname": "Петров",
            "name": "Петр",
            "fathername": "Петрович",
            "telefon": 89270020202,
            "comment": "телефон Петрова"
        },
        {
            "id": 3,
            "surname": "Степанов",
            "name": "Степан",
            "fathername": "Степанович",
            "telefon": 89270030303,
            "comment": "телефон Степанова"
        },
        {
            "id": 4,
            "surname": "Сидоров",
            "name": "Иван",
            "fathername": "Петрович",
            "telefon": 89270040404,
            "comment": "телефон Сидорова"
        }
    ]
    return test_dict
    # try:
    #     import json                                                     # импортируем библиотеку
    #     # Действие 1 - считать исходную БД в переменную
    #     with open(name_path_file, "r", encoding="UTF-8") as my_file:    # читаем из файла
    #         string_json = my_file.read()
    #     list_readed_dicts = json.loads(string_json)                      # проводим десериализацию JSON-объекта
        
    #     # Если случайно предали искомое как словарь - перезапись его в списк из словарей
    #     if (type(record) is dict):
    #         record = [record]

    #     result = []
    #      # Действие 2 - Поиск по критерию в списке словарей (БД из файла)
    #     if (condition_to_find[0])['surname'] != "":
    #         for i in list_readed_dicts:
    #             find_what = list_readed_dicts
    #             find_where = list_readed_dicts
    #             if ((condition_to_find[0])['surname']).upper() in (str(k)).upper()):
    #                 result[]
    #                 break

    #     elif (condition_to_find[0])['name'] != "":

    #     elif (condition_to_find[0])['fathername'] != "":

    #     elif (condition_to_find[0])['telefon'] != 0:

    #     elif (condition_to_find[0])['comment'] != "":




    #     # Действие 2.1 - Поиск индекса списка по номеру id
    #     index_of_record_with_needed_id = -1                             # если такого id нет, то редактировать не можем
    #     # Если случайно предали искомое как словарь - перезапись его в списк из словарей
    #     if (type(record) is dict):
    #         record = [record]
    #     id_record_to_modify = (record[0])['id']                         # вытащено id из словаря/списка, выбранного пользователем на изменение
    #     for i in range(0, len(list_readed_dicts)):                      
    #         if (list_readed_dicts[i])['id'] == id_record_to_modify:                
    #             index_of_record_with_needed_id = i
    #             break  # так как id уникальный первичный ключ, одинаковых значений не может быть
    #     # Действие 2.2 - Непосредственное редактирование по найденномув п. 2.1 индексу (уже не по не id)
    #     if index_of_record_with_needed_id == -1:
    #         return -1    #если не нашли id в справочнике для удаления, то выходим с отрицательным результатом выполнения
    #     i = index_of_record_with_needed_id
    #     # !!!!Вот это очень нехорошая часть!!!!!
    #     # так как при изменении сруктуры БД (+- столбец|ключ) всё полетит
    #     # for key, value in users.items(): print(f"Phone: {key}  User: {value} ")  не даст сразу 2 перебрать
    #     if (record[0])['surname'] != "":
    #         (list_readed_dicts[i])['surname'] = (record[0])['surname']
    #     if (record[0])['name'] != "":
    #         (list_readed_dicts[i])['name'] = (record[0])['name']
    #     if (record[0])['fathername'] != "":
    #         (list_readed_dicts[i])['fathername'] = (record[0])['fathername']
    #     if (record[0])['telefon'] != 0:
    #         (list_readed_dicts[i])['telefon'] = (record[0])['telefon']
    #     if (record[0])['comment'] != "":
    #         (list_readed_dicts[i])['comment'] = (record[0])['comment']
    #      # Действие 3 - Перезаписать полностью обновлённую БД с отсутсвием удалённой записи
    #     string_json = json.dumps(list_readed_dicts, indent=4, ensure_ascii=False) # десериализация в строку json
    #     with open(name_path_file, "w", encoding="UTF-8") as my_file:
    #         my_file.write(string_json)
    #     return list_readed_dicts
    # except:
    #     return -1

def m_print_db(db_list_of_dicts: list):
    if len(db_list_of_dicts) < 1:
        return -1
    for i in range(0, 86):
        print('═', end = "")
    print("")
    print("║{:^6}".format('id'), end = "|")
    print("{:^15}".format('Фамилия'), end = "|")
    print("{:^10}".format('Имя'), end = "|")
    print("{:^15}".format('Отчество'), end = "|")
    print("{:^13}".format('Телефон'), end = "|")
    print("{:^20}".format('Комментарий'), end = "║")
    print("")
    for i in range(0, 86):
        print('═', end = "")
    print("")
    for i in range(0, len(db_list_of_dicts)-1):
        print("║{:^6}".format(str((db_list_of_dicts[i])['id'])), end = "|")
        print("{:^15}".format(str((db_list_of_dicts[i])['surname'])), end = "|")
        print("{:^10}".format(str((db_list_of_dicts[i])['name'])), end = "|")
        print("{:^15}".format(str((db_list_of_dicts[i])['fathername'])), end = "|")
        print("{:^13}".format(str((db_list_of_dicts[i])['telefon'])), end = "|")
        print("{:^20}".format(str((db_list_of_dicts[i])['comment'])), end = "║")
        print("")
        for i in range(0, 86):
            print('─', end = "")
        print("")
    else:
        j = len(db_list_of_dicts)-1
        print("║{:^6}".format(str((db_list_of_dicts[j])['id'])), end = "|")
        print("{:^15}".format(str((db_list_of_dicts[j])['surname'])), end = "|")
        print("{:^10}".format(str((db_list_of_dicts[j])['name'])), end = "|")
        print("{:^15}".format(str((db_list_of_dicts[j])['fathername'])), end = "|")
        print("{:^13}".format(str((db_list_of_dicts[j])['telefon'])), end = "|")
        print("{:^20}".format(str((db_list_of_dicts[j])['comment'])), end = "║")
        print("")
        for i in range(0, 86):
            print('═', end = "")
        print("")

def create_dict(id:int, surname:str, name:str, fathername:str, telefon:int, comment:str):
    ''' 
    функция-консруктор - для создания словаря по аргументам, в соответсвие с столбцами таблицы БД
    
    Вход:
        корректный набор данных строк и целых чисел, при этом отсутсвующие не допускаются
        вызывающий должен направить хотя бы пустое значение
    Возвращает:
        успешное выполнение - словарь, заполненнымй значениями (аргументами) со входа
        сбой в заполении - (-1), как индикатор сбоя операции заполнения словаря аргументами
    '''
    try:  # на случай, если не передали какой-то аргумент для заполнения словаря значениямм
        mydict = {
            'id': id,
            'surname': surname,
            'name': name,
            'fathername': fathername,
            'telefon': telefon,
            'comment': comment
        }
    except:
        return -1     # сбой выполнения
    return mydict     # штатное выполнение

def create_dict_empty():
    ''' 
    функция-консруктор - для создания пустого словаря, в соответсвие с столбцами таблицы БД
    Вход:
       отсутсвует
    Возвращает:
        пустой словарь для дальнейшего его заполненнения
    '''
    mydict = {
        'id': 0,
        'surname': "",
        'name': "",
        'fathername': "",
        'telefon': 800000000000,
        'comment': ""
    }
    return mydict



# def renumirate_id_column(list_db : list) -> list:
#     ''' 
#     функция для перенумерации id по порядку в bd

#     Вход:
#        список словарей - исходная база данных
#     Возвращает:
#         пустой словарь для дальнейшего его заполненнения
#     Пояснение:
#         1. Окрытие файла на чтение .json
#         2. Сохранение в типе данных json
#         3. Закрытие файла .json
#         4. Поиск строк по нужному критерию
#         5. Формирование нового словаря из результата поиска
#     '''


# передача небольшой функции в качестве аргумента:
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# pairs
# -> [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# Небольшие анонимные функции могут быть созданы с помощью lambda. 
# Эта функция возвращает сумму двух своих аргументов: lambda a, b: a+b. 
# Лямбда-функции можно использовать везде, где требуются функциональные объекты.
# Они синтаксически ограничены одним выражением. 
# Семантически они являются просто синтаксическим сахаром для обычного определения функции. 
# Как и определения вложенных функций, 
# лямбда-функции могут ссылаться на переменные из содержащей области:
# def make_incrementor(n):
#     return lambda x: x  + n
# f = make_incrementor(42)
# f(0)   ->   42
# f(1)   ->   43






# #****************************************************************************** 
# #********************************* НАЧАЛО ТЕСТОВ ****************************** 
# #****************************************************************************** 

# print("\n Выполнение тестов")

# def give_me_any_list_of_dict():

#     test_dict = [
#         {
#             "id": 1,
#             "surname": "Иванов",
#             "name": "Иван",
#             "fathername": "Иванович",
#             "telefon": 89270010101,
#             "comment": "телефон Иванов"
#         },
#         {
#             "id": 2,
#             "surname": "Петров",
#             "name": "Петр",
#             "fathername": "Петрович",
#             "telefon": 89270020202,
#             "comment": "телефон Петрова"
#         },
#         {
#             "id": 3,
#             "surname": "Степанов",
#             "name": "Степан",
#             "fathername": "Степанович",
#             "telefon": 89270030303,
#             "comment": "телефон Степанова"
#         },
#         {
#             "id": 4,
#             "surname": "Сидоров",
#             "name": "Иван",
#             "fathername": "Петрович",
#             "telefon": 89270040404,
#             "comment": "телефон Сидорова"
#         }
#     ]
#     return test_dict

# ## Получить список по умолчанию из 4-х записей/словарей
# dict_test = give_me_any_list_of_dict()
# # print("\nPRIMARY (not file) dict_test = ", dict_test)
# name_file = "test_alex.json"

# #****************************************************************************** 
# #************ ТЕСТ № 1 - ДОБАВЛЕНИЕ В КОНЕЦ ТЕЛЕФОННОГО СПРАВОЧНИКА *********** 
# #****************************************************************************** 
# # #для добавления в конец
# # dict_to_add = [
# #         {
# #             "id": 1,
# #             "surname": "Иванов",
# #             "name": "Иван",
# #             "fathername": "Иванович",
# #             "telefon": 89270010101,
# #             "comment": "телефон Иванов"
# #         }
# # ]
# # print("\ndict_to_add = ", dict_to_add)
# # #Добавление новой записи в конец
# # dict_test_updated = m_adding(name_file, dict_test)
# # print("\ndict_test_updated = ", dict_test_updated)

# #****************************************************************************** 
# #******** ТЕСТ № 2 - УДАЛЕНИЕ ЗАПИСИ ПО ID В ТЕЛЕФОННОМ СПРАВОЧНИКЕ *********** 
# #****************************************************************************** 
# # # Удаление записи по номеру id
# # dict_test_minus_one_by_id = m_delete(name_file, 5)
# # print("\n dict_test_minus_one_by_id = ", dict_test_minus_one_by_id)

# #****************************************************************************** 
# #******** ТЕСТ № 3 - ИЗМЕНЕНИЕ ЗАПИСИ ПО ID В ТЕЛЕФОННОМ СПРАВОЧНИКЕ ********** 
# #****************************************************************************** 
# # Список из словарей для изменения
# list_dict_with_changes = [
#         {
#             "id": 1,
#             "surname": "Гвидонов",
#             "name": "Гвидон",
#             "fathername": "Гвидонович",
#             "telefon": 0,
#             "comment": ""
#         }
# ]
# # Словарь для изменения
# dict_with_changes = \
#         {
#             "id": 1,
#             "surname": "Словарёв",
#             "name": "Словарь",
#             "fathername": "Словаревич",
#             "telefon": 0,
#             "comment": "Демо со словарём"
#         }

# # ! сначала нужн очистить файл "test_alex.json"
# m_adding(name_file, give_me_any_list_of_dict())

# # демонстрация успеха с списком словарей в аргументах
# dict_test_midifited_by_id = m_edit(name_file, list_dict_with_changes)
# print("\n Успех со списком - dict_test_midifited_by_id = ", dict_test_midifited_by_id)

# # демонстрация провала с списком словарей в аргументах (т.к. записи нет с id = 100)
# list_dict_with_changes_second = list_dict_with_changes
# (list_dict_with_changes_second[0])['id'] = 100
# dict_test_midifited_by_id = m_edit(name_file, list_dict_with_changes_second)
# print("\nПровал - dict_test_midifited_by_id = ", dict_test_midifited_by_id)

# # демонстрация успеха с словарём в аргументах
# dict_test_midifited_by_id = m_edit(name_file, dict_with_changes)
# print("\n Успех со словарём - dict_test_midifited_by_id = ", dict_test_midifited_by_id)

# # демонстрация успеха с списком словарей в аргументах
# (list_dict_with_changes[0])['id'] = 1
# dict_test_midifited_by_id = m_edit(name_file, list_dict_with_changes)
# print("\n Успех со списком - dict_test_midifited_by_id = ", dict_test_midifited_by_id)

# #****************************************************************************** 
# #************ ТЕСТ № 4 - ПОИСК ЗАПИСИ  В ТЕЛЕФОННОМ СПРАВОЧНИКЕ *************** 
# #****************************************************************************** 



# #****************************************************************************** 
# #*************************** ТЕСТ № 5 - Показать БД *************************** 
# #****************************************************************************** 

# list_dict_show = [
#         {
#             "id": 1,
#             "surname": "Гвидонов",
#             "name": "Гвидон",
#             "fathername": "Гвидонович",
#             "telefon": 88552336699,
#             "comment": "домашний"
#         },
#         {
#             "id": 2,
#             "surname": "Иванов",
#             "name": "Сидр",
#             "fathername": "Гаврилович",
#             "telefon": 89196008585,
#             "comment": "сотовый"
#         },
#         {
#             "id": 3,
#             "surname": "Петров",
#             "name": "Константин",
#             "fathername": "Александрович",
#             "telefon": 89196008585,
#             "comment": "сотовый"
#         }
# ]
# m_print_db(list_dict_show)

# print("\nЗавершение тестов\n ")

# #****************************************************************************** 
# #********************************* КОНЕЦ ТЕСТОВ ****************************** 
# #****************************************************************************** 