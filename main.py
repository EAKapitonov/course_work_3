from utils_classes.utils import import_data, sort_operations
import json

"""
Открываем файл json,  декодируем в объекты python
передаем функции import_data для получения необходимого типов данных 
    """
with open("operations.json", 'r', encoding='UTF-8') as f:
    data_operations = json.load(f)
    list_operations_class = import_data(data_operations)
    sorted_list_operations_class = sort_operations(list_operations_class)

i = 0
x = 5
while i < x:
    if sorted_list_operations_class[i].state != "EXECUTED":
        x += 1
        i += 1
        continue
    else:
        print(sorted_list_operations_class[i].print_date_description())
        print(sorted_list_operations_class[i].print_transfer_to() + " -> " + sorted_list_operations_class[
            i].print_transfer_from())
        print(sorted_list_operations_class[i].print_operationAmount())
        print()
        i += 1
