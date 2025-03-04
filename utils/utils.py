import hashlib

class Utils:
    @staticmethod
    def transactionHash(self):
        data = "this is a bank simulation"
        data_hash = hashlib.sha256(data.encode()).hexdigest()

        return data_hash