class Item:
    def __init__(self, weight, value, symbol):
        self.weight = weight
        self.value = value
        self.symbol = symbol

def knapsack(items, capacity):
    def node_bound_count(i, weight, value):
        if weight > capacity:
            return 0
        node_value = value
        j = i
        total_weight = weight

        while j < len(items) and total_weight + items[j].weight <= capacity:
            node_value += items[j].value
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            node_value += (capacity - total_weight) * (items[j].value / items[j].weight)

        return node_value

    def branch_bound(i, weight, value):
        nonlocal max_value, best_combination
        if weight <= capacity and value > max_value:
            max_value = value
            best_combination = current_combination.copy()
        if i == len(items):
            return
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i + 1, weight, value)
        if value + (capacity - weight) * (items[i].value / items[i].weight) > max_value:
            current_combination.append(items[i].symbol)
            branch_bound(i + 1, weight + items[i].weight, value + items[i].value)
            current_combination.pop()

    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    best_combination = []
    current_combination = []
    branch_bound(0, 0, 0)
    return max_value, best_combination

if __name__ == '__main__':
    items = [
        Item(3, 25, 'r'),  # Винтовка
        Item(2, 15, 'p'),  # Пистолет
        Item(2, 15, 'a'),  # Боекомплект
        Item(2, 20, 'm'),  # Аптечка
        Item(1, 5, 'i'),   # Ингалятор
        Item(1, 15, 'k'),  # Нож
        Item(3, 20, 'x'),  # Топор
        Item(1, 25, 't'),  # Оберег
        Item(1, 15, 'f'),  # Фляжка
        Item(1, 10, 'd'),  # Антидот
        Item(2, 20, 's'),  # Еда
        Item(2, 20, 'c'),  # Арбалет
    ]

# Основное заадние

    capacity = 8
    max_value, best_combination = knapsack(items, capacity)

    inventory = [['' for _ in range(4)] for _ in range(2)]  # 2x4
    idx = 0
    for symbol in best_combination:
        row = idx // 4
        col = idx % 4
        inventory[row][col] = symbol
        idx += 1

    for row in inventory:
        print('[' + '],['.join(row) + ']')
    print(f'Итоговые очки выживания: {max_value}')


# # Дополнительное задание 1

#     capacity = 7
#     max_value, best_combination = knapsack(items, capacity)

#     inventory = [['' for _ in range(4)] for _ in range(2)]  # 2x4
#     idx = 0
#     for symbol in best_combination:
#         row = idx // 4
#         col = idx % 4
#         inventory[row][col] = symbol
#         idx += 1

#     if max_value > 0:
#         for row in inventory:
#             print('[' + '],['.join(row) + ']')
#         print(f'Итоговые очки выживания: {max_value}')
#     else:
#         print("Нет решения: невозможно собрать положительное количество очков выживания.")


# # Дополнительное задание 2

#     combinations = knapsack(items, capacity)

#     if combinations:
#         print("Положительные комбинации предметов:")
#         for combination in combinations:
#             print(combination)
#     else:
#         print("Нет положительных комбинаций предметов.")