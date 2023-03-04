class Operation():
    """
    Класс экземпляром которого является 1 операция из источника
    """
    def __init__(self, id: int, state: str, date: str, operationAmount: dict, description: str, transfer_from: str,
                 transfer_to: str):
        self.id = id
        self.state = state
        self.date = date
        self.operationAmount = operationAmount
        self.description = description
        self.transfer_from = transfer_from
        self.transfer_to = transfer_to

    def __repr__(self):
        return f"{self.description}\nid операции -  {self.id} \nдата - {self.date[0:10]}"


    def print_date_description(self):
        """

        :return: дату и тип операции в нужном формате для отображения клиенту
        """
        i = self.date
        return i[8] + i[9] + "." + i[5] + i[6] + "." + i[0] + i[1] + i[2] + i[3] + " " + self.description

    def print_transfer_from(self):
        """

        :return: источник перевода в нужном формате для отображения клиенту
        """
        i = self.transfer_from
        x = i.split(" ")
        if len(x) == 3:
            return x[0] + " " + x[1] + " " + x[2][0:4] + " " + x[2][4:6] + "** **** " + x[2][12:16]
        if len(x) == 2:
            if len(x[1]) == 20:
                return x[0] + " **" + x[1][16:20]
            if len(x[1]) == 16:
                return x[0] + " " + x[1][0:4] + " " + x[1][4:6] + "** **** " + x[1][12:16]

    def print_transfer_to(self):
        """

        :return: получатель перевода в нужном формате для отображения клиенту
        """
        i = self.transfer_to
        x = i.split(" ")
        if len(x) == 3:
            return x[0] + " " + x[1] + " " + x[2][0:4] + " " + x[2][4:6] + "** **** " + x[2][12:16]
        if len(x) == 2:
            if len(x[1]) == 20:
                return x[0] + " **" + x[1][16:20]
            if len(x[1]) == 16:
                return x[0] + " " + x[1][0:4] + " " + x[1][4:6] + "** **** " + x[1][12:16]

    def print_operationAmount(self):
        """

        :return: сумму перевода в нужном для отображения клиенту формате
        """
        i = self.operationAmount["amount"]
        z = self.operationAmount["currency"]["name"]
        return i + " " + z
