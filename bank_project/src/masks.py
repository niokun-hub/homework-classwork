def get_mask_card_number(card_number: str):

    first_part = card_number[:4]
    second_part = card_number[4:6]
    last_part = card_number[-4:]
    return f"{first_part} {second_part}** **** {last_part}"


def get_mask_account(account_number: str):
    last_digits = account_number[-4:]

    return f"**{last_digits}"



if __name__ == "__main__":
    print("Маскировка карт и счета")

    print("\n1. Маскировка карты")
    card_number = "7000792289606361"
    print(f"Входной номер: {card_number}")
    print(f"Результат:     {get_mask_card_number(card_number)}")

    print("\n2. Маскировка счета")
    account_number = "73654108430135874305"
    print(f"Входной номер: {account_number}")
    print(f"Результат:     {get_mask_account(account_number)}")