# 1.1 Создает кортеж a_tuple, элементами которого являются объекты следующих типов:
#     2 - число с плавающей запятой
#     5 - список
#     4 - строка
#     3 - логическое значение

a_tuple = (43.3, [True, 32, "Box"], "Moon", False)
print("Созданный кортеж: ", a_tuple)

# 1.2 Изменяет значение одного из элементов объекта a_tuple
# путем преобразования его сначала в список, а затем снова в кортеж.

a_list = list(a_tuple)
a_list[2] = [a_list[2]]
a_list[2].append(67)
a_tuple = tuple(a_list)
print("Измененный кортеж: ", a_tuple, "\n")

# 1.3 Создает объект a_range диапазона:
#   -10, 10

a_range = range(-10, 10)

# 1.4 Выводит на экран значения объекта a_range, используя (см. колонку "Вывод" табл. №1):
#     1 - оператор for

print("Значения диапазона: ")
for i in a_range:
    print(i, end=" ")
Код задания 2:
    # 2.1 Выполняет все функции программы "ana.py". При этом формирует до пяти анаграмм средней сложности
# (степень сложности определяет студент).

# 2.2 Расширяет функциональность программы следующим образом:
#   Вариант 1 – если пользователь дал правильное решение, то ему предоставляется возможность выбрать более
#               сложный вариант анаграммы (всего три уровня сложности);

import random


def anagrams(word):
    ang = ""
    while word:
        pos = random.randrange(len(word))
        ang += word[pos]
        word = word[:pos] + word[pos + 1:]
    return ang


words_tuples = ('коллекция', 'монитор', 'сервер', 'диапазон', 'задача'
)
new_word = random.choice(words_tuples)
correct_answer = new_word

game_lvl = 1
anagram = anagrams(new_word)
print('Вот анаграмма: ', anagram)
answer = input('Попробуй отгадать слово: ')

while True:
    if answer != correct_answer and answer != '':
        print('Ответ неправильный')
        answer = input('Попробуй еще раз: ')
    else:
        print('Молодец!')
        if game_lvl != 3:
            next_lvl = input("Не хочешь продолжить и перейти к более сложной анаграмме? (Да/Нет) : ")
            if next_lvl == "Да":
                game_lvl += 1
                new_word = random.choice(words_tuples)
                correct_answer = new_word
                for i in range(game_lvl):
                    new_word = anagrams(new_word)
                anagram = new_word
                print('Вот новая анаграмма: ', anagram)
                answer = input('Попробуй теперь отгадать слово: ')
            else:
                break
        if game_lvl == 3:
            print("\nУра! Ты прошел все уровни!")
            break
print('Спасибо за игру!')
