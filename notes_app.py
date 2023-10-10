import json
import datetime

# Функция для создания новой заметки
def create_note(notes):
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

# Функция для чтения списка заметок
def read_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Функция для удаления заметки по id
def delete_note(notes):
    note_id = int(input("Введите id заметки для удаления: "))
    note = next((note for note in notes if note["id"] == note_id), None)
    
    if not note:
        print("Заметки с таким id не существует.")
        return
    
    notes.remove(note)
    save_notes(notes)
    print("Заметка успешно удалена.")

# Функция для редактирования заметки по id
def edit_note(notes):
    note_id = int(input("Введите id заметки для редактирования: "))
    note = next((note for note in notes if note["id"] == note_id), None)

    if not note:
        print("Заметки с таким id не существует.")
        return
    
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note["title"] = title
    note["body"] = body
    note["timestamp"] = timestamp

    save_notes(notes)
    print("Заметка успешно отредактирована.")

# Функция для вывода списка заметок в от старых к новым
def list_notes_decending(notes):
    for note in sorted(notes, key=lambda x: x["timestamp"]):
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки: {note['body']}")
        print(f"Дата создания: {note['timestamp']}\n")

# Функция для вывода списка заметок с фильтрацией по дате
def list_notes(notes):
    filter_date_str = input("Введите дату для фильтрации (ГГГГ-ММ-ДД): ")
    
    try:
        filter_date = datetime.datetime.strptime(filter_date_str, "%Y-%m-%d")
    except ValueError:
        print("Некорректный формат даты. Используйте ГГГГ-ММ-ДД.")
        return
    
    filtered_notes = [note for note in notes if filter_date.date() == datetime.datetime.strptime(note["timestamp"], "%Y-%m-%d %H:%M:%S").date()]
    
    if not filtered_notes:
        print("Заметок на выбранную дату нет.")
        return
    
    for note in filtered_notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело заметки: {note['body']}")
        print(f"Дата создания: {note['timestamp']}\n")
