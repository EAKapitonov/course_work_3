from utils_classes.utils import import_data, sort_operations

data_url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677914845650&signature=pZ9lTOxZ6PV_ku_O6n-azlpZf9PwxkKAAxfiEbTt77w&downloadName=operations.json"
list_operations_class = import_data(data_url)
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
