# Попробовать решить задачи включениями и lambda-функциями (ЕСЛИ
# ЭТО ВОЗМОЖНО).
# 1. Создайте список всех чисел от 1 до 30 включительно, которые
# делятся на 3.
print('Задание 1:')
lst = [x for x in range(30+1) if x % 3 == 0]
print(lst)
print()

# 2. Создайте список цифр числа 12345.
print('Задание 2:')
digits = list(map(int,str(12345)))
print(digits)
print()

# 3. Создайте список сумм цифр чисел от 10 до 20 включительно.
print('Задание 3:')
digits = [el for el in range(10, 20+1)]
print(sum(digits))
print()

# 4. Создайте список всех чисел от 1 до 50 включительно, которые
# содержат цифру 3. (‘3’ in str(13) подсказка интересного решения)
print('Задание 4:')
lst = [el for el in range(1, 50+1) if '3' in str(el)]
print(lst)
print()

# 5. Создайте список кортежей, где каждый кортеж состоит из числа от 1
# до 10 включительно и его квадрата.
print('Задание 5:')
lst = [(el, el**2) for el in range(1, 10+1)]
print(lst)
print()

# 6. Напишите lambda-функцию, которая принимает два числа и
# возвращает их произведение.
print('Задание 6:')
lst = lambda a, b: a * b
print(lst(2, 6))
print()

# 7. Напишите lambda-функцию, которая принимает три числа и
# возвращает их сумму.
print('Задание 7:')
lst = lambda a, b, c: a + b + c
print(lst(2, 5, 75))
print()

# 8. Напишите lambda-функцию, которая принимает два логических
# значения и возвращает их логическое И.
print('Задание 8:')
lst = lambda a, b: a and b
print(lst(True, False))
print()


# 9. Используйте lambda и функцию filter(), чтобы оставить в списке
# только числа, кратные 4.
print('Задание 9:')
numbers = [1, 4, 7, 12, 36]
filt_num = filter(lambda x: x % 4 == 0, numbers)
print(list(filt_num))
print()


# 10.Используйте lambda и функцию map(), чтобы возвести каждый
# элемент в списке в куб.
print('Задание 10:')
numbers = [1, 12, 344]
res = list(map(lambda x: x ** 3, numbers))
print(res)