immutable_var = (1, 2, 3, True, 'Julia', 0.56, [2, 4, 6])
print(immutable_var)
immutable_var[-1][-1] = 10
print(immutable_var)
#значение элементов кортежа нельзя изменить потому что он относится к неизменяемым типам данных,
# это позволяет нам использовать кортеж в качестве хранилища для особенно важных данных, которые должны быть защищены от вмешательства
# однако мы можем изменять элементы внетреннего списка кортежа, как показано на примере выше

mutable_list = [1, 2, 3, 4, 5]
mutable_list[0] = 55
mutable_list.append('Urban')
mutable_list.pop(3)
print(mutable_list)

