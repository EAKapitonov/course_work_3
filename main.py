import requests
from utils_classes.class_operation import Operation
data_url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677914845650&signature=pZ9lTOxZ6PV_ku_O6n-azlpZf9PwxkKAAxfiEbTt77w&downloadName=operations.json"
file = requests.get(data_url)
list_operations_dict = file.json()
print(list_operations_dict)
list_operations_class = []
for i in list_operations_dict:
    print(i['id'])
    operation = Operation(i['id'], i['state'], i['date'], i['operationAmount'], i['description'], i['from'], i['to'])
    list_operations_class.append(operation)

print(list_operations_class)