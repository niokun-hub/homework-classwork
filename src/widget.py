from masks import get_mask_card_number, get_mask_account
def mask_account_card(account_info: str):

    words = account_info.split()
    number = words[-1]
    card_type = " ".join(words[:-1])


    if card_type.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"


if __name__ == "__main__":

    print("\n1. КАРТА VISA")
    result1 = mask_account_card("Visa Platinum 7000792289606361")
    print(f"Вход:  Visa Platinum 7000792289606361")
    print(f"Выход: {result1}")


    print("\n2. КАРТА MAESTRO")
    result2 = mask_account_card("Maestro 7000792289606361")
    print(f"Вход:  Maestro 7000792289606361")
    print(f"Выход: {result2}")

    print("\n3. БАНКОВСКИЙ СЧЕТ")
    result3 = mask_account_card("Счет 73654108430135874305")
    print(f"Вход:  Счет 73654108430135874305")
    print(f"Выход: {result3}")
