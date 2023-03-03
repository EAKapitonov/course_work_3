import requests
from utils_classes.class_operation import Operation
def import_data(data_url):
    """

    :param url_data:
    :return:
    """
    file = requests.get(data_url)
    list_operations_dict = file.json()
    list_operations_class = []
    for i in list_operations_dict:
        if len(i.keys()) != 7:
            continue
        operation = Operation(i['id'], i['state'], i['date'], i['operationAmount'], i['description'], i['from'], i['to'])
        list_operations_class.append(operation)
    return list_operations_class

def sort_operations(list_operations_class):
    """

    :param list_operations_class:
    :return:
    """
    list_date = []
    sorted_list_operations_class = []
    for i in list_operations_class:
        list_date.append(i.date)

    list_date.sort()

    for i in list_date:
        for x in list_operations_class:
            if x.date == i:
                sorted_list_operations_class.append(x)
                break

    return sorted_list_operations_class