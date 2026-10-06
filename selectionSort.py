from typing import List


class SelectionSort:
    sortedList: List[int] = []
    def __init__(self, unsortedList: List[int]):
        self.unsortList = unsortedList
        self.sortedList = unsortedList.copy()
        
    def __str__(self):
        return (str(self.unsortList))
        
    def sort(self):
        for scope in range(len(self.sortedList) - 1, 0, -1):
            index = scope
            for i in range(scope):
                if(self.sortedList[i] > self.sortedList[index]):
                    index = i
            self.sortedList[scope], self.sortedList[index] = self.sortedList[index], self.sortedList[scope]
                
        
    

newSelect = SelectionSort([6,9,2,1,5,61])

newSelect.sort()
print(newSelect) 
print(newSelect.sortedList) 

