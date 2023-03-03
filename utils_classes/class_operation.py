class Operation():
    def __init__(self, id:int, state:str, date:str, operationAmount:dict, description:str, transfer_from:str, transfer_to:str):
        self.id = id
        self.state = state
        self.date = date
        self.operationAmount = operationAmount
        self.description = description
        self.transfer_from = transfer_from
        self.transfer_to = transfer_to

    def print_date_description(self):
        """

        :return:
        """
        i = self.date
        print(i[8] + i[9] + "." + i[5] + i[6] + "." + i[0] + i[1] + i[2] + i[3] + " " + self.description)

    def print_transfer_from(self):
        """

        :return:
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

        :return:
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

        :return:
        """
        i = self.operationAmount["amount"]
        z = self.operationAmount["currency"]["name"]
        return i+" "+z