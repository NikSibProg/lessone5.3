#
# *Дополнительное задание:
#
# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют
# общие характеристики, такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс Store, который можно будет использовать
# для создания различных магазинов.

class Store:
    def __init__(self, name, address):
        """
        Конструктор для инициализации магазина с названием, адресом и пустым ассортиментом товаров.
        """
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров (ключ — название, значение — цена)

    def add_item(self, item_name, price):
        """
        Метод для добавления товара в ассортимент магазина.
        """
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """
        Метод для удаления товара из ассортимента магазина.
        """
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_item_price(self, item_name):
        """
        Метод для получения цены товара по его названию.
        Возвращает None, если товар не найден.
        """
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """
        Метод для обновления цены товара.
        Если товара нет в ассортименте, выводится сообщение об ошибке.
        """
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def display_items(self):
        """
        Метод для отображения всех товаров и их цен.
        """
        if not self.items:
            print("Ассортимент пуст.")
        else:
            print(f"Товары в магазине '{self.name}':")
            for item_name, price in self.items.items():
                print(f"- {item_name}: {price}")

# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями,
# адресами и добавь в каждый из них несколько товаров.

# Создаем первый магазин
store1 = Store("Магазин Продукты", "ул. Ленина, д. 1")
store1.add_item("хлеб", 0.8)
store1.add_item("молоко", 1.2)
store1.add_item("яйца", 1.5)

# Создаем второй магазин
store2 = Store("Магазин Фрукты", "ул. Гагарина, д. 5")
store2.add_item("яблоки", 0.5)
store2.add_item("бананы", 0.75)
store2.add_item("апельсины", 1.1)

# Создаем третий магазин
store3 = Store("Магазин Одежда", "пр. Победы, д. 10")
store3.add_item("футболка", 15.0)
store3.add_item("джинсы", 35.0)
store3.add_item("куртка", 55.0)

# Отображаем ассортимент каждого магазина
print("\nАссортимент магазина 1:")
store1.display_items()

print("\nАссортимент магазина 2:")
store2.display_items()

print("\nАссортимент магазина 3:")
store3.display_items()

# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй
# все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.

# Тестирование методов

# Добавляем новый товар
store1.add_item("сыр", 2.5)
print("\nПосле добавления товара 'сыр':")
store1.display_items()

# Обновляем цену товара 'хлеб'
store1.update_item_price("хлеб", 1.0)
print("\nПосле обновления цены товара 'хлеб':")
store1.display_items()

# Удаляем товар 'молоко'
store1.remove_item("молоко")
print("\nПосле удаления товара 'молоко':")
store1.display_items()

# Запрашиваем цену товара 'яйца'
price_eggs = store1.get_item_price("яйца")
print(f"\nЦена товара 'яйца': {price_eggs}")

# Запрашиваем цену товара, которого нет в магазине
price_milk = store1.get_item_price("молоко")
print(f"Цена товара 'молоко': {price_milk}")  # Должно вывести None, так как молоко было удалено
