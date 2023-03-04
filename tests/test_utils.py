from utils_classes.utils import import_data, sort_operations
import json
import pytest
@pytest.fixture
def list_operations_class_test():
    with open("operations_test.json", 'r', encoding='UTF-8') as f:
        data_operations = json.load(f)
        list_operations_class_test = import_data(data_operations)
    return list_operations_class_test
def test_import_data(list_operations_class_test):
    """
    Проверяет функцию import_data, сравнивая с известными данными
    """
    assert list_operations_class_test[0].date == "2019-08-26T10:50:58.294041"
    assert list_operations_class_test[1].date == "2019-07-03T18:35:29.512364"
    assert list_operations_class_test[2].date == "2018-06-30T02:08:58.425572"
    assert list_operations_class_test[3].date == "2019-04-04T23:20:05.206878"

@pytest.fixture
def sorted_list_operations_class_test():
    with open("operations_test.json", 'r', encoding='UTF-8') as f:
        data_operations = json.load(f)
        list_operations_class_test = import_data(data_operations)
        sorted_list_operations_class_test = sort_operations(list_operations_class_test[1:10])
    return sorted_list_operations_class_test
def test_sort_operations(sorted_list_operations_class_test):
    """
    Проверяет функцию sort_operations, сравнивая с известными данными
    """

    assert sorted_list_operations_class_test[0].date == "2019-07-12T20:41:47.882230"
    assert sorted_list_operations_class_test[1].date == "2019-07-03T18:35:29.512364"
    assert sorted_list_operations_class_test[2].date == "2019-04-04T23:20:05.206878"
    assert sorted_list_operations_class_test[3].date == "2019-03-23T01:09:46.296404"
