import json

def load_data():
    try:
        with open("data.json", "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"balance": 0, "operations": []}

def save_data(data):
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False