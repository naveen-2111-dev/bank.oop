import uuid

class Utils:
    @staticmethod
    def transactionhash():
        return str(uuid.uuid4())