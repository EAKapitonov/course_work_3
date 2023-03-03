class Operation():
    def __init__(self, id:int, state:str, date:str, operationAmount:dict, description:str, transfer_from:str, transfer_to:str):
        self.id = id
        self.state = state
        self.date = date
        self.operationAmount = operationAmount
        self.description = description
        self.transfer_from = transfer_from
        self.transfer_to = transfer_to
