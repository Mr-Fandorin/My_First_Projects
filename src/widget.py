import re

import masks

def mask_account_card(card_account_num: str) -> str:
    """Функция маскирующая номер счета или карты"""
    if re.search('[а-яА-Я]', card_account_num):
        split_card_account_num = card_account_num.split()
        mask_account_num = masks.get_mask_account(int(split_card_account_num[-1]))
        split_card_account_num.remove(split_card_account_num[-1])
        split_card_account_num.append(mask_account_num)
        str_mask_account = ' '.join(split_card_account_num)
        return str_mask_account
    else:
        split_card_account_num = card_account_num.split()
        mask_card_num = masks.get_mask_card_number(int(split_card_account_num[-1]))
        split_card_account_num.remove(split_card_account_num[-1])
        split_card_account_num.append(mask_card_num)
        str_mask_card = ' '.join(split_card_account_num)
        return str_mask_card



