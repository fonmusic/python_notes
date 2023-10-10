from notes_app import (
    create_note,
    delete_note,
    edit_note,
    list_notes_decending,
    list_notes,
    read_notes,
)

def main():
    try:
        notes = read_notes()
    except FileNotFoundError:
        notes = []

    while True:
        print("Выберите команду:")
        print("1. Добавить новую заметку")
        print("2. Удалить заметку")
        print("3. Редактировать заметку")
        print("4. Вывести список заметок (от старых к новым)")
        print("5. Вывести список заметок (с фильтрацией по дате)")
        print("6. Выход")
        
        command = input("Введите команду: ")
         
        if command == "1":
            create_note(notes)
        elif command == "2":
            delete_note(notes)
        elif command == "3":
            edit_note(notes)
        elif command == "4":
            list_notes_decending(notes)
        elif command == "5":
            list_notes(notes)
        elif command == "6":
            break
        else:
            print("Некорректная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
