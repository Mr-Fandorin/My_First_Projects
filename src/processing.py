def filter_by_state(list_of_dicts_id: list, state="EXECUTED") -> list:
    """Функция, фильтрующая словари по нужному ключу"""
    new_list_of_dicts = []
    for i in list_of_dicts_id:
        for value in i.values():
            if value == state:
                new_list_of_dicts.append(i)
    return new_list_of_dicts


def sort_by_date(list_of_dicts_id: list, sorting_type=True) -> list:
    """Функция, сортирующая словари по нужному ключу"""
    sorted_list_of_dict = sorted(list_of_dicts_id, key=lambda dict_id: dict_id["date"], reverse=sorting_type)
    return sorted_list_of_dict
