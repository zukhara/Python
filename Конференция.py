def calculate_ticket_cost(age):
    if age < 18:
        return 0  # Бесплатно для лиц младше 18 лет
    elif 18 <= age < 25:
        return 990  # 990 руб. для лиц от 18 до 25 лет
    else:
        return 1390  # 1390 руб. для лиц от 25 лет и старше

def main():
    try:
        num_tickets = int(input("Введите количество билетов: "))
        total_cost = 0

        for _ in range(num_tickets):
            age = int(input("Введите возраст посетителя: "))
            ticket_cost = calculate_ticket_cost(age)
            total_cost += ticket_cost

        # Применяем скидку 10% при заказе более трех билетов
        if num_tickets > 3:
            total_cost *= 0.9

        print(f"Общая стоимость билетов: {total_cost} руб.")

    except ValueError:
        print("Ошибка: Введите корректное число билетов и возраста.")

if __name__ == "__main__":
    main()