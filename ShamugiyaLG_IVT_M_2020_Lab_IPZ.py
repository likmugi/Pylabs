class ExceptionNoDots(Exception):
    pass

class ExceptionIsDigit(Exception):
    pass

# Считываем имя файла
file_name = input("Введите имя файла: ")

# Считываем расширение
try:

    if file_name.find(".") == -1:
        raise ExceptionNoDots('File extension delimiter "." not found.')

    if not set("'\\'/:*?<>|").isdisjoint(file_name):
        raise ValueError("The file name cannot contain special characters.")

    file_extension = file_name.split(".")[-1]

    if file_extension.isdigit():
        raise ExceptionIsDigit("The file extension cannot contain only numbers.")

except ExceptionNoDots:
    print("В имени отсутвует расширение файла.")

except ExceptionIsDigit:
    print("Расширение не может состоять из цифр")

except ValueError:
    print("Имя файла не может содержать специальных символов.")

else:
    print(file_extension)
