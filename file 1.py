# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
def odd_nams(max_num):
    for num in range(1,max_num+1,2):
        yield num


odd_nams_20=odd_nams(20)
print(type(odd_nams_20))
print(*odd_nams_20,sep=' ')


