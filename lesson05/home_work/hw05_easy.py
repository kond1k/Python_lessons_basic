import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def create_folder(num):
    dir_path = os.path.join(os.getcwd(), 'NewDir' + str(num))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')


def delete_folder(num):
    dir_path = os.path.join(os.getcwd(), 'NewDir' + str(num))
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Такой папки не существует')


create_folder(1)
create_folder(2)
delete_folder(1)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def show_folder():
    print(*os.listdir(os.getcwd()))


show_folder()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(num):
    shutil.copyfile(__file__, __file__ + str(num))


copy_file(1)
