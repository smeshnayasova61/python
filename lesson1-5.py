#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

n = input('Введите значение выручки фирмы: ')
print(n)
m = input('Введите значение выручки фирмы: ')
print(m)
if (n > m):
    print('Прибыль')
elif (n < m):
    print('Убыток')
else:
    print('Ноль - тоже хороший результат! Рост впереди!')