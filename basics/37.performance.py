# ADVANCE: COMPARE TIMINGS different solutions
import timeit
setup_code = '''
numbers = [8,1,19,20,30,40,1,5,6,7,99,2,20, 0,15,30,50,60,70,80,105,231,123123,12312314, 93945834,345,34,543,534,534,534,5,345,34,534,5,34,543,5,34,534,5,34,564,6,54,756756,7,567567,567,56,7567567567567567,567567567567567,567567567567456345,634534534534534,534534534534534,53453453453453,4534543,5435345,34645756785,68678678678678,678678]
'''
mycode1 = '''
def find_max90(numbers):
    numbers.sort()
    return numbers.__getitem__(-1)
'''
mycode2 = '''
def find_max99(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value
'''
mycode3 = '''
def f3():
    max(numbers)
'''
mycode4 = '''
max(numbers)
'''

print(timeit.timeit(setup=setup_code, stmt=mycode1, number=10000000))
print(timeit.timeit(setup=setup_code, stmt=mycode2, number=10000000))
print(timeit.timeit(setup=setup_code, stmt=mycode3, number=10000000))
print(timeit.timeit(setup=setup_code, stmt=mycode4, number=10000000))
