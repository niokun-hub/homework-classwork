def get_mask_card_number(card_number: str):

    first_part = card_number[:4]
    second_part = card_number[4:6]
    last_part = card_number[-4:]
    return f"{first_part} {second_part}** **** {last_part}"


def get_mask_account(account_number: str):
    last_digits = account_number[-4:]

    return f"**{last_digits}"



