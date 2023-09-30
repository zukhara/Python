def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Возвращаем индекс элемента, который больше или равен целевому числу

def main():
    try:
        input_sequence = input("Введите последовательность чисел через пробел: ")
        target_number = float(input("Введите число для поиска: "))

        # Преобразуем введенную последовательность в список чисел
        numbers = [float(num) for num in input_sequence.split()]

        # Сортируем список по возрастанию
        numbers.sort()

        # Ищем позицию элемента с помощью двоичного поиска
        position = binary_search(numbers, target_number)

        # Проверяем, что элемент на позиции position меньше введенного числа, и следующий за ним больше или равен
        if position < len(numbers) and numbers[position] < target_number:
            position += 1

        if position < len(numbers):
            result = numbers[position]
            print(f"Ближайший элемент, меньший или равный {target_number}, это {result}")
        else:
            print("Нет элементов, удовлетворяющих условию.")

    except ValueError:
        print("Ошибка: Пожалуйста, введите корректные числа.")

if __name__ == "__main__":
    main()