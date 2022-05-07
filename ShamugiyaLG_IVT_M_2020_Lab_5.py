import math
import collections.abc

# 1. Определена и выполнена функция func1() с аргументами в виде списка чисел (целых и с плавающей точкой), которая выполняет:
#     3 – определение квадратных корней элементов списка

def func1(lists):
    sqrt_list = [round(math.sqrt(x), 4) for x in lists] # round() использовалась для улучшения читабельности результата
    return sqrt_list

print("Задание 1.")

func1_list = [12, 3.2, 54, 87, 95.4, 6]
print(f"Квадратные корни элементов списка: \n"
      f"{func1(func1_list)} \n")

# 2.1 Создан словарь a_dict (числом элементов не меньше 8), ключи которого именуются произвольно, а значения заданы в виде:
#     1 – латинские буквы
# При этом отдельные ключи (числом не меньше трех) должны иметь одинаковое значение.

a_dict = {'1': 'o', '2': 't', '3': 'p', '4': 'y', '5': 't', '6': 'h', '7': 't', '8': 'o', '9': 'n'}

# 2.2 Определена функция func2(), которая имеет два аргумента, первый – в виде словаря, второй – указывает значение
# ключа словаря. func2() возвращает список ключей словаря, значения которых совпадают со значениями второго аргумента.

def func2(dictionary, input_key):
    keys_list = []
    for key in dictionary.keys():
        if dictionary[key] == dictionary[input_key] and key != input_key:
            keys_list.append(key)
    return keys_list

print("Задание 2.")
k = input("Введите ключ (от 1 до 9): ")
print(f"Со значением вашего ключа совпадают значения {func2(a_dict,k)} ключей \n")

# 3.1 Создан список a_list, элементы которого имеют тип:
#     2 – логические значения;
#     5 – списки с элементами в виде строк.

a_list = [True, ["1", "2"], True, False, ["3", "4"]]

# 3.2 Определена функция func3(), которая преобразует каждый элемент заданного списка a_list в целое число (механизм
# преобразования – на усмотрение студента).

def func3(n_list):
    int_n_list = []
    for item in n_list:
        if isinstance(item, collections.abc.MutableSequence):
            for x_in_item in item:
                int_n_list.append(int(x_in_item))
        else:
            int_n_list.append(int(item))
    return int_n_list

# 3.3 Выполнена с использованием функции func3() и метода sort() сортировка элементов списка a_list:
#     для четных номеров индивидуального задания – по возрастанию;
int_a_list = func3(a_list)
int_a_list.sort(reverse=False)
print("Задание 3. \n" + str(int_a_list) + "\n")

# 4.1 Задана строка str_code, содержащая небольшой фрагмент кода на языке Python и получен скомпилированный с помощью
# встроенной функции compile() код – comp_code.

print("Задание 4.")
str_code = 'print("Я - небольшой фрагмент кода на языке Python")\n' \
           'z = 5 \n' \
           'print(f"И я умею считать: {z} + 1 = {z+1}")'
comp_code = compile(str_code, '<string>', 'exec')

# 4.2 С помощью встроенной функции exec() код comp_code исполнить.

exec(comp_code)
