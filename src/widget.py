import re

import masks


def mask_account_card(card_account_num: str) -> str:
    """Функция маскирующая номер счета или карты"""
    if re.search("[а-яА-Я]", card_account_num):
        mask_account_num = masks.get_mask_account(int(card_account_num[-20:]))
        return f"{card_account_num[:-20]}{mask_account_num}"
    else:
        mask_card_num = masks.get_mask_card_number(int(card_account_num[-17:]))
        return f"{card_account_num[:-17]} {mask_card_num}"


def get_date(full_date: str) -> str:
    """Функция упрощающая вид даты"""
    part_full_date = full_date[:10]
    split_date = part_full_date.split("-")
    rev_list_date = split_date[-1:-4:-1]
    short_date = ".".join(rev_list_date)
    return short_date
