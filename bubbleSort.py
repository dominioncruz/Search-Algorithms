class BubbleSort:
    
    def __init__(self, unsortedList):
        self.unsortList = unsortedList
        
    def __str__(self):
        return (str(self.unsortList))
        
    def sort(self):
        for scope in range(len(self.unsortList) - 1, 0, -1):
            for i in range(scope):
                if(self.unsortList[i] > self.unsortList[i + 1]):
                    self.unsortList[i], self.unsortList[i + 1] = self.unsortList[i + 1], self.unsortList[i]
                
        
    

newBubble = BubbleSort([4,1,6,20,2,5])

newBubble.sort()
print(newBubble) 

