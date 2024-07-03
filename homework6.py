my_dict = {'Julia': 1990,
           'Anna': 1992,
           'Denis': 1994,
           'Serge': 1988}
print(my_dict)
print(my_dict['Julia'])
print(my_dict.get('Piter'))
my_dict.update({'Egor': 2001,
                'Mark': 2000})
print(my_dict)
a = my_dict.pop('Julia')
print(a)
print(my_dict)

my_set = {1, 2, 3, 1, 4, 1, 5, 2, 3, 'Julia', 'Urban', 'Julia'}
print(my_set)
my_set.add(6)
my_set.add('Ivan')
my_set.discard(3)
print(my_set)
