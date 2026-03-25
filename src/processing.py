def filter_by_state(transactions, state="EXECUTED"):
    new_list = []
    for item in transactions:
        if item.get("state") == state:
            new_list.append(item)
    return new_list


def sort_by_date(transactions, reverse=True):
    new_list = transactions.copy()
    for i in range(len(new_list)):
        for j in range(i + 1, len(new_list)):
            if reverse:
                if new_list[i]["date"] < new_list[j]["date"]:
                    new_list[i], new_list[j] = new_list[j], new_list[i]
            else:
                if new_list[i]["date"] > new_list[j]["date"]:
                    new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list


if __name__ == "__main__":
    transactions = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000", "amount": 5000},
        {"id": 2, "state": "CANCELED", "date": "2024-01-10T14:20:00.000", "amount": 1000},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-20T09:15:00.000", "amount": 2500}
    ]

    print(filter_by_state(transactions))
    print(filter_by_state(transactions, "САNCELED"))
    print(sort_by_date(transactions))
    print(sort_by_date(transactions, False))