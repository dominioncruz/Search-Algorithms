class InsertionSort:
    
    def __init__(self, unsortedList):
        self.unsortList = unsortedList
        
    def __str__(self):
        return (str(self.unsortList))
        
    def sort(self):
        for valueToCompreWith in range(1, len(self.unsortList)):
            
            j = valueToCompreWith
            
            while(self.unsortList[j] < self.unsortList[j - 1] and j > 0):
                self.unsortList[j], self.unsortList[j - 1] = self.unsortList[j - 1], self.unsortList[j]
                j = j - 1
                
        
    

newInsertionSort = InsertionSort([4,1,6,20,2,5])

newInsertionSort.sort()
print(newInsertionSort) 

