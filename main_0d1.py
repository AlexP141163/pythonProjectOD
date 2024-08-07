# Палиндромы - это текстовая строка которая одинаково читается как в прямом направлении так и обратном.
# Приведение строки к единому регистру: Поскольку палиндромы не зависят от регистра символов,
# все символы строки нужно привести к нижнему регистру.
# Импортируем модуль 're' -  в Python, он предоставляет функции для работы с регулярными выражениями.
# Регулярные выражения используются для поиска, замены и манипуляции строками на основе шаблонов.
# Для нашей задачи мы будем использовали re.sub, чтобы удалить все неалфавитные символы из строки,
# т.е. для удаления всех символов, кроме букв латинского алфавита.
# Сравниваем строку с её обратной версией. Если они равны, возвращаем True, иначе False.

import re

def is_palindrome(s):
    # Приводим строку к нижнему регистру
    s = s.lower()

    # Удаляем все неалфавитные символы
    s = re.sub(r'[^a-z]', '', s)
    # Сравниваем строку с её обратной версией
    return s == s[::-1]

# Примеры использования
print(is_palindrome("A man, A plan, A canal, Panama"))  # True
print(is_palindrome("Hello, World!"))                   # False