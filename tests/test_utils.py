from utils_classes.utils import import_data, sort_operations
from main import data_url

def test_import_data():
    """
    Проверяет функцию import_data, сравнивая с известными данными
    """
    list_operations_class_test = import_data(data_url)
    assert list_operations_class_test[2].date == "2018-06-30T02:08:58.425572"
    assert list_operations_class_test[3].date == "2019-04-04T23:20:05.206878"
    assert list_operations_class_test[4].date == "2019-03-23T01:09:46.296404"
    assert list_operations_class_test[5].date == "2018-12-20T16:43:26.929246"
    assert list_operations_class_test[6].date == "2019-07-12T20:41:47.882230"
    assert list_operations_class_test[7].date == "2018-08-19T04:27:37.904916"


def test_sort_operations():
    """
    Проверяет функцию sort_operations, сравнивая с известными данными
    """
    list_operations_class_test = import_data(data_url)
    sorted_list_operations_class_test = sort_operations(list_operations_class_test[1:10])
    assert sorted_list_operations_class_test[2].date == "2019-04-04T23:20:05.206878"
    assert sorted_list_operations_class_test[3].date == "2019-03-23T01:09:46.296404"
    assert sorted_list_operations_class_test[4].date == "2018-12-20T16:43:26.929246"
    assert sorted_list_operations_class_test[5].date == "2018-09-12T21:27:25.241689"
    assert sorted_list_operations_class_test[6].date == "2018-08-19T04:27:37.904916"
    assert sorted_list_operations_class_test[7].date == "2018-06-30T02:08:58.425572"