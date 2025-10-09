def get_mask_card_number(card_number: int) -> str:
    """Функция, маскирующая номер карты"""
    str_card_number = str(card_number)
    mask_card_number = str_card_number.replace(str_card_number[6:12], "******")
    return f"{mask_card_number[:4]} {mask_card_number[4:8]} {mask_card_number[8:12]} {mask_card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция, маскирующая номер карты"""
    str_account_number = str(account_number)
    return f"**{str_account_number[-4:]}"
