def open_file() -> list:
#Открывает файл в формате списка
    with open("S_task_8_49_contact.txt", "r", encoding="utf-8") as file:
        return (contact_list := list(file))
    

print(open_file())

