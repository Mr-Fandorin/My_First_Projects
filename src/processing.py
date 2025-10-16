def filter_by_state(list_of_dicts_id: list, state="EXECUTED") -> list:
    """Функция, фильтрующая словари по нужному ключу"""
    new_list_of_dicts = []
    for i in list_of_dicts_id:
        for value in i.values():
            if value == state:
                new_list_of_dicts.append(i)
    return new_list_of_dicts
