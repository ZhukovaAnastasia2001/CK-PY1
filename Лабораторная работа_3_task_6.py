list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
list_index = list(range(len(list_numbers)))  # назначим индекс каждому значению (начиная с 0)

# Находим индекс последнего максимального элемента списка

max_index = 0
max_number = list_numbers[max_index]

for i, current_number in enumerate(list_numbers):
    max_number = list_numbers[max_index]
    if current_number >= max_number:
        max_index = i
        max_number = list_numbers[max_index]

# Индекс последнего элемента 19

# Меняем последний максимальный элемент и последний элемент местами

list_numbers[max_index], list_numbers[19]= list_numbers[19], list_numbers[max_index]

print(list_numbers)
# Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
