from apyori import apriori

class apriori_recommendation(object):
    def __init__(self,input_item,transactions,records=[]):
        self.input_item = input_item
        self.transactions= transactions
        self.records=records
        
    def build_freq_item_set(self):
        records = []
        self.transactions= self.transactions.fillna(0)
        row,col = self.transactions.shape
        for i in range(0,self.transactions.shape[0]):
            records.append([str(self.transactions.values[i,j]) for j in range(0,col) if str(self.transactions.values[i,j]) != '0'])
        return records
    
    def prep_hyperparameters(self):
        support = 0
        for s in range(0,col):
            support +=self.transactions[s][self.transactions[s] == input_item].count()      
        return support
                                
    def get_association(self):
        association_rules = apriori(self.records, min_support=0.0045, min_confidence=0.2, min_lift=2, min_length=2)  
        return list(association_rules)
    
    def run(self):
        recommendation_items = []
        self.records = self.build_freq_item_set()
        association_results = self.get_association()
        for item in association_results:
            p = item[0]
            items = [x for x in p]    
            if self.input_item in items:
                print(items)
                recommendation_items+=items
                print('support -> ' +  str(item[1])  + ': confidence -> ' + str(item[2][0][2]) + ': lift -> ' + str(item[2][0][3]))
        unique_items= set(recommendation_items)
        unique_items.remove(self.input_item)
        return unique_items
    
        
        
        
        
        