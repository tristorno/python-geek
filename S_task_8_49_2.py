def save_file(contact_list: list) -> str:
    with open("S_task_8_49_contact.txt", "w", encoding="utf-8") as file:
        file.write(" ".join(contact_list.join(" ")))

    return "Файл сохранен"

contact_list = ["Иванов Иван 6877786"]
print(contact_list)
print(save_file(contact_list))