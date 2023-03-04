from utils_classes.utils import import_data, sort_operations
import json
import pytest
@pytest.fixture
def sorted_list_operations_class_test():
    with open("operations_test.json", 'r', encoding='UTF-8') as f:
        data_operations = json.load(f)
        list_operations_class_test = import_data(data_operations)
        sorted_list_operations_class_test = sort_operations(list_operations_class_test)
        return sorted_list_operations_class_test
def test_operation(sorted_list_operations_class_test):
    """
    проверяет корректность создания объектов класса Operation
    """
    assert sorted_list_operations_class_test[2].id == 41428829
    assert sorted_list_operations_class_test[2].state == "EXECUTED"
    assert sorted_list_operations_class_test[2].date == "2019-07-03T18:35:29.512364"
    assert sorted_list_operations_class_test[2].operationAmount == {'amount': '8221.37', 'currency': {'code': 'USD', 'name': 'USD'}}
    assert sorted_list_operations_class_test[2].description == "Перевод организации"
    assert sorted_list_operations_class_test[2].transfer_from == "MasterCard 7158300734726758"
    assert sorted_list_operations_class_test[2].transfer_to == "Счет 35383033474447895560"
    assert sorted_list_operations_class_test[2].print_transfer_from() == "MasterCard 7158 30** **** 6758"
    assert sorted_list_operations_class_test[2].print_date_description() == "03.07.2019 Перевод организации"
    assert sorted_list_operations_class_test[2].print_transfer_to() == "Счет **5560"
    assert sorted_list_operations_class_test[2].print_operationAmount() == "8221.37 USD"


