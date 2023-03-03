from utils_classes.utils import import_data, sort_operations
from utils_classes.class_operation import Operation
data_url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677914845650&signature=pZ9lTOxZ6PV_ku_O6n-azlpZf9PwxkKAAxfiEbTt77w&downloadName=operations.json"
list_operations_class = import_data(data_url)
sorted_list_operations_class = sort_operations(list_operations_class)

"""Принт Дата и тип перевода"""
i = sorted_list_operations_class[1].date
print(i[8]+i[9]+"."+i[5]+i[6]+"."+i[0]+i[1]+i[2]+i[3]+" "+sorted_list_operations_class[1].description)

"""Принт счета"""
i = sorted_list_operations_class[1].transfer_from
x, y = i.split(" ")
print(x+" **"+y[16:20])

i = sorted_list_operations_class[2].transfer_from
print(i)