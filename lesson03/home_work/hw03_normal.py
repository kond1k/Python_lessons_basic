# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fib = []
    count = 2
    fib1 = 1
    fib2 = 1

    while count < m:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        count += 1
        if count >= n:
            fib.append(fib2)
    return fib


print(fibonacci(4, 9))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    i = 0
    j = 0
    save = 0
    first = 0
    second = 0
    while i < len(origin_list) - 1:
        while j < len(origin_list) - 1:
            if origin_list[j] < origin_list[j + 1]:
                save = origin_list[j]
                origin_list[j] = origin_list[j + 1]
                origin_list[j + 1] = save
            j += 1
        i += 1
        j = 0
    print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, iter):
    back = []
    for elem in iter:
        if func(elem):
            back.append(elem)
    return back


numbers = range(-5, 5)
my_f = lambda x: x < 0
print(my_filter(my_f, numbers))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parall(A1, A2, A3, A4):
    top = ((A2[0] - A1[0]) ** 2 + (A2[1] - A1[1]) ** 2) ** (1 / 2)
    bot = ((A4[0] - A3[0]) ** 2 + (A4[1] - A3[1]) ** 2) ** (1 / 2)
    right = ((A3[0] - A2[0]) ** 2 + (A3[1] - A2[1]) ** 2) ** (1 / 2)
    left = ((A1[0] - A4[0]) ** 2 + (A1[1] - A4[1]) ** 2) ** (1 / 2)
    return top == bot and right == left


print(is_parall((-3, 11), (12, -4), (1, -7), (-14, 8)))
