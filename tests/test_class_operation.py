from utils_classes.utils import import_data, sort_operations
from main import data_url


def test_operation():
    """

    :return:
    """
    list_operations_class_test = import_data(data_url)
    sorted_list_operations_class_test = sort_operations(list_operations_class_test)
    assert sorted_list_operations_class_test[2].id == 154927927
    assert sorted_list_operations_class_test[2].state == "EXECUTED"
    assert sorted_list_operations_class_test[2].date == "2019-11-19T09:22:25.899614"
    assert sorted_list_operations_class_test[2].operationAmount == {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}
    assert sorted_list_operations_class_test[2].description == "Перевод организации"
    assert sorted_list_operations_class_test[2].transfer_from == "Maestro 7810846596785568"
    assert sorted_list_operations_class_test[2].transfer_to == "Счет 43241152692663622869"


