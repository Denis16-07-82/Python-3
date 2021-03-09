# *(вместо 1) Решить задачу генерации нечётных чисел
# от 1 до n (включительно), не используя ключевое слово yield.
while True:
    num = float(input('Введите целое число n ,больше 0: '))
    if  num.is_integer() and num > 0:
        odd_nams_n = (num for num in range(1, int(num) + 1, 2))
        break
    else:
        print('Вы ввели число не правильно')
print(type(odd_nams_n),*odd_nams_n,sep=' ')
