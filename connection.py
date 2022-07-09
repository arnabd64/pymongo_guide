import pymongo

class Connection:
    
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client['Accounting']
        self.master = self.db['MasterChartOfAccounts']
        self.custom = self.db['CustomChartOfAccounts']
        self.ledger = self.db['Ledger']
        
        
