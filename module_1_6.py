my_dict = {'Sofia': 2002, 'Ivan': 2017}
print(my_dict)
print(my_dict['Ivan'])
print(my_dict.get('Max'))
my_dict.update({'Irina': 1997,
                'Dima': 1990})
a = my_dict.pop('Sofia')
print(a)
print(my_dict)

my_set = {12, 1, 4, 5, 2, 12, 1, 4, 'Ivan', 'Max', 'Ivan', 'Irina'}
print(my_set)
my_set.add(7)
my_set.add(9)
my_set.discard(12)
print(my_set)