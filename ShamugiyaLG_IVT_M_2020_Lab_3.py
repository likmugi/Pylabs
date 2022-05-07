import collections.abc as ABC

# 1. Создает список a_list, элементами которого являются объекты типов: int, float, bool, str и list

a_list = [12, 23.4, True, "Python", [45.2, 3, 6.4]]
print("Задание 1.")
print("Создали список:")
print(" ", a_list, "\n")

# 2. Для каждого элемента списка a_list определяет:
# тип элемента и ABC-класс (если элемент принадлежит к некоторому ABC-классу).

print("Задание 2.")
print("Определяем типы элеметов списка:")
print(" ", [type(x) for x in a_list])
print("Определяем ABC-класс элементов:")
for x in a_list:
    if isinstance(x, ABC.Hashable):
        print(f"  {x} - тип {str(type(x))[slice(8, -2)]} - принадлежит классу Hashable")
    elif isinstance(x, ABC.Sequence):
        print(f"  {x} - тип {str(type(x))[slice(8, -2)]} - принадлежит классу Sequence")
    elif isinstance(x, ABC.Iterable):
        print(f"  {x} - тип {str(type(x))[slice(8, -2)]} - принадлежит классу Iterable")
print("")

# 3. Для списка a_list выполняет операции:
#     3 - s.append(x)
#     7 - s.remove(x)
#     8 - s.reverce()

print("Задание 3.")
a_list.append("String")
a_list.remove(12)
a_list.reverse()
print("После выполнения  ряда операций, список выглядит следующим образом: ")
print(a_list, "\n")

# 4. Создает строку s, содержащую слова или числа:
#   Содержимое - числа
#   Разделитель - символ "#"

print("Задание 4.")
numbers_list = [252, 53, 36, 243, 546, 31]
numbers_string = [str(x) for x in numbers_list]
delimiter = "#"
s = delimiter.join(numbers_string)
print("Получили из списка строку: ", s, "\n")

# 5. Преобразует строку s в список b_list

print("Задание 5.")
b_list = s.split(sep="#")
b_list = [int(x) for x in b_list]
print("Преобразовали строку обратно в список: ", b_list)
print("")

# 6. Выполняет над элементами списка b_list функции len(), min()

len_b_list = len(b_list)
min_b_list = min(b_list)

# 7. Выводит результаты выполнения функций на экран.

print("Задания 6-7.")
print("Количество элементов в списка: ", len_b_list)
print("Элемент списка с минимальным значением: ", min_b_list)
