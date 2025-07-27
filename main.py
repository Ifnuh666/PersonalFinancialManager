from utils import load_data, save_data
from datetime import datetime
from tabulate import tabulate

def main():
    data = load_data()

    while True:
        print("\n1. Добавить операцию\n2. История\n3. Статистика\n4. Выход")
        choice = input("> ")

        if choice == "1":
            add_operations(data)
        elif choice == "2":
            show_history(data)
        elif choice == "3":
            result = statistics(data)
            print(f"Максимальная операция: {result} ₽" if result else "Нет данных для статистики")
        elif choice == "4":
            save_data(data)
            break

# Функция для добавления данных
def add_operations(data):
    op_type = input("Доход / Расход: ").lower()
    amount = int(input("Сумма: "))
    category = input("Категория: ")
    comment = input("Комментарий к покупке: ")

    # Добавляем в список данные
    data["operations"].append({
        "type": op_type,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "comment": comment
    })

    # Обновляем баланс
    if op_type == "Доход":
        data["balance"] += amount
    else:
        data["balance"] -= amount

# Функция для просмотра истории
def show_history(data):
    if not data["operations"]:
        print("История операций пуста")
        return
    # Подготовка данных для таблицы
    headers = ["Дата", "Тип", "Сумма", "Категория", "Комментарий"]
    rows = []
    
    for op in data["operations"]:
        rows.append([
            op["date"],
            op["type"],
            f"{op['amount']} ₽",
            op["category"],
            op.get("comment", "")
        ])
    
    # Вывод таблицы с сортировкой по дате (новые сверху)
    print(tabulate(sorted(rows, key=lambda x: x[0], reverse=True), headers=headers))

# Функция для просмотра статистики
def statistics(data):
    if not data.get("operations"):
        print("Нет операций для анализа")
        return None
    try:
        return max(op["amount"] for op in data["operations"])
    except (KeyError, TypeError):
        return None
        


if __name__ == "__main__":
    main()