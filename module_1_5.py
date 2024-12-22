immutable_var = (1.2, 4, True, 'string')
print(immutable_var)
# Кортеж не изменяемый тип данных.
immutable_list = list(immutable_var)
immutable_list[2] = 'Истина'
print(immutable_list)