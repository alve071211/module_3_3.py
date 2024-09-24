def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(5,5)
print_params(7,8,2)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [35, 'осень', False]
values_dict = {'a':'лето', 'b': 30.5, 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [77, 'строчечка']

print_params(*values_list_2,42)