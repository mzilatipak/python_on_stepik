# -*- coding: utf-8 -*-
# 13.1.1
""" Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
def draw_box():
    print('*' * 10)             # 1
    print('*', ' ' * 6, '*')    # 2
    print('*', ' ' * 6, '*')    # 3
    print('*', ' ' * 6, '*')    # 4
    print('*', ' ' * 6, '*')    # 5
    print('*', ' ' * 6, '*')    # 6
    print('*', ' ' * 6, '*')    # 7
    print('*', ' ' * 6, '*')    # 8
    print('*', ' ' * 6, '*')    # 9
    print('*', ' ' * 6, '*')    # 0
    print('*', ' ' * 6, '*')    # 1
    print('*', ' ' * 6, '*')    # 2
    print('*', ' ' * 6, '*')    # 3
    print('*' * 10)             # 4

draw_box() """

# 13.1.2
""" Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10 в соответствии с образцом:
*
**
***
****
*****
******
*******
********
*********
**********
def draw_triangle():
    for i in range(1, 11):
        print('*' * i)

draw_triangle() """

# 13.2.1
""" # Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
# Примечание. Гарантируется, что основание треугольника – нечетное число.
# объявление функции
def draw_triangle(fill, base):
    for i in range(0, base // 2 + 1):
        for j in range(0, i+1):
            print(fill, end='')
        print()
    for k in range(base // 2-1, -1, -1):
        for l in range(0, k+1):
            print(fill, end = '')
        print()
# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base) """

# 13.2.2
""" # Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра: 
# name – имя человека; 
# surname – фамилия человека; 
# patronymic – отчество человека; 
# а затем выводит на печать ФИО человека.
# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0], name[0], patronymic[0], sep='')

# считываем данные
name, surname, patronymic = input().upper(), input().upper(), input().upper()

# вызываем функцию
print_fio(name, surname, patronymic) """

# 13.2.3
""" # Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
# объявление функции
def print_digit_sum(num):
    summ = 0  # локальная переменная
    while num != 0:
        last = num % 10  # последня цифра в n(um)
        # summ += last  # сумма
        summ += num % 10
        num //= 10  # обрезаем последнюю цифру у n(um)
    print(summ)

# считываем данные
n = int(input())  # глобальная переменная

# вызываем функцию
print_digit_sum(n) """
# Все операции в теле функции мы выполняем с её параметром. В данном случае def print_digit_sum(num):  
# именно с num. А когда идет вызов функции, именно в этот момент заместо num подставляется n. 

# 13.4.1
""" # Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах 
# и возвращает расстояние в милях. Формула для преобразования: мили = километры * 0.6214.
# Примечание. Следующий программный код:
# print(convert_to_miles(1))
# print(convert_to_miles(5))
# print(convert_to_miles(10))
# должен выводить:
# 0.6214
# 3.107
# 6.214
# объявление функции
def convert_to_miles(km):
    return km * 0.6214

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num)) """

# 13.4.2
""" # Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и 
# возвращает количество дней в данном месяце.
# Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
# Примечание 2. Считайте, что год является невисокосным.

# объявление функции
def get_days(month):
    if num == 1 or num == 3 or num == 5 or num == 7 or num == 8 or num == 10 or num == 12:
        return 31
    elif num == 4 or num == 6 or num == 9 or num == 11:
        return 30
    else:
        return 28

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num)) """

# 13.4.3
""" # Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и 
# возвращающую список всех делителей данного числа.
# объявление функции
def get_factors(num):
    lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    return lst

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n)) """

# 13.4.4
""" # Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и 
# возвращающую количество делителей данного числа.

# объявление функции
def number_of_factors(num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n)) """

# 13.4.5
""" # Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа "a" в строке. 
# Проблема заключается в том, что данный метод не находит местоположение всех символов "а".
# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: 
# строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.
# Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.
# объявление функции
def find_all(target, symbol):
    lst = []
    for i in range(len(target)):
        if target[i] == symbol:
            lst.append(i)
    return lst

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char)) """

# 13.4.6
""" # Напишите функцию merge(list1, list2), 
# которая принимает в качестве аргументов два отсортированных по возрастанию списка, 
# состоящих из целых чисел, и объединяет их в один отсортированный список.
# Примечание 1. Списки list1 и list2 могут иметь разную длину.
# Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.

# объявление функции
def merge(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2)) """

# 13.4.7
""" # На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания. 
# Из данных строк формируются списки чисел. 
# Напишите программу, которая объединяет указанные списки в один отсортированный список 
# с помощью функции quick_merge(), а затем выводит его.

# объявление функции
def quick_merge(list):
    list1 = []
    for _ in range(n):
        list_nums = [int(el) for el in input().split()]
        list1 += list_nums
    list1.sort()
    return list1

n = int(input())

print(*quick_merge(list)) """

# 13.5.1
""" # Напишите функцию is_valid_triangle(side1, side2, side3), 
# которая принимает в качестве аргументов три натуральных числа, 
# и возвращает значение True если существует невырожденный 
# треугольник со сторонами side1, side2, side3 и False в противном случае.
def is_valid_triangle(side1, side2, side3):
    # return a + b > c and a + c > b and b + c > a - так лучше
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())  # считывает данные

print(is_valid_triangle(a, b, c)) 

# ещё вариант:
# объявление функции
def is_valid_triangle():
    # считываем данные
    a, b, c = int(input()), int(input()), int(input())
    return a + b > c and a + c > b and b + c > a

# вызываем функцию
print(is_valid_triangle())"""

# 13.5.2 *
""" # Напишите функцию is_prime(num), 
# которая принимает в качестве аргумента натуральное число и возвращает значение True, 
# если число является простым и False в противном случае.
# объявление функции
def is_prime(num):
    lst = []  # можно через счётчик, если каунт == 2 и тэдэ
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    if len(lst) == 2:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n)) """

# 13.5.3 **
""" # Напишите функцию get_next_prime(num), 
# которая принимает в качестве аргумента натуральное число num и 
# возвращает первое простое число большее числа num.
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

# объявление функции
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

def get_next_prime(num):
    num = num + 1
    while is_prime(num) != True:
        num += 1
        if is_prime(num) == True:
            break
    return num

# считываем данные
n = int(input())

# вызываем функцию
# print(is_prime(n))
print(get_next_prime(n)) """
# нахождение простоого числа следующего за введённым, одной функцией
""" # объявление функции
def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n)) """

# 15.5.4 *
""" #Напишите функцию is_password_good(password), 
# которая принимает в качестве аргумента строковое значение пароля password 
# и возвращает значение True, если пароль является надежным и False - в противном случае.
# Пароль является надежным если:
# 1. его длина не менее 8 символов; 
# 2. он содержит как минимум одну заглавную букву (верхний регистр); 
# 3. он содержит как минимум одну строчную букву (нижний регистр);
# 4. он содержит хотя бы одну цифру.

def is_password_good(password):
    if len(password) < 8:
        return False
    count1, count2, count3 = 0, 0, 0
    for i in range(len(password)):
        if password[i].isdigit():
            count1 += 1
        elif password[i].islower():
            count2 += 1
        elif password[i].isupper():
            count3 += 1
    if count1 >= 1 and count2 >= 1 and count3 >= 1:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt)) """

# 15.5.5
""" # Напишите функцию is_one_away(word1, word2), 
# которая принимает в качестве аргументов два слова word1 и word2 
# и возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в 1 символе 
# и False - в противном случае.

def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2)) """

# 15.5.6 *
""" # Напишите функцию is_palindrome(text), 
# которая принимает в качестве аргумента строку text и возвращает значение True 
# если указанный текст является палиндромом и False в противном случае.
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, 
# а также игнорируйте пробелы, а также символы , . ! ? -.

def is_palindrome(text):
    text1 = ''
    for i in range(len(text)):  #собрали строку из букв
        if text[i].isalpha():
            text1 += text[i].lower()
    print(text1)
    if text1[:] == text1[::-1]:
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt)) """

# 15.5.7
""" # BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. 
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), 
# которая принимает в качестве аргумента строковое значение пароля password 
# и возвращает значение True, если пароль является действительным паролем BEEGEEK банка 
# и False - в противном случае.

def is_valid_password(password):
    lst = password.split(':')
    if len(lst) != 3:
        return False
    count = 0
    a, b, c = ''.join(lst[0]), int(''.join(lst[1])), int(''.join(lst[2]))
    for i in range(2, b + 1):
            if b % i == 0:
                count += 1
    for _ in range(1):
        if a[:] == a[::-1] and c % 2 == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

psw = input()

print(is_valid_password(psw)) """

# 15.5.8 *
""" # Напишите функцию is_correct_bracket(text), 
# которая принимает в качестве аргумента непустую строку text, 
# состоящую из символов "(" и ")" и возвращает значение True, 
# если поступившая на вход строка является правильной скобочной последовательностью 
# и False в противном случае.
# Примечание. Правильной скобочной последовательностью называется строка, 
# состоящая только из символов "(" и ")", где каждой открывающей скобке найдется парная закрывающая скобка 
# (при этом каждая открывающая скобка должна быть левее соответствующей ей закрывающей скобки).

def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
        print(text)
    if len(text) == 0:
        return True
    else: 
        return False

txt = input()

print(is_correct_bracket(txt)) """

# 15.5.9
""" # Напишите функцию convert_to_python_case(text), 
# которая принимает в качестве аргумента строку в «верблюжьем регистре» 
# и преобразует его в «змеиный регистр».
# ThisIsCamelCased => this_is_camel_cased
# IsPrimeNumber => is_prime_number

def this_is_camel_cased(text):
    lst = []
    for i in range(len(text)):
        if text[i].islower() or text[i].isdigit():
            lst.append(text[i])
        else:
            lst.append('_')
            lst.append(text[i].lower())
    return lst[1:]        

# txt = input()
txt = 'ThisIsCamelCased'

print(*this_is_camel_cased(txt), sep='') """

# 16..




