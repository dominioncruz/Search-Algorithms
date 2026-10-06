class BinSearch:

    def __init__(self, orderedList):
        self.orderedList = orderedList

    def __str__(self):
        return self.orderedList
    
    def compare(self, reducedList, value):
        if len(reducedList) == 0: 
            print("not found")
            return
        else:
            index = len(reducedList) // 2
            if(value > reducedList[index]):
                self.compare(reducedList[index + 1:], value)
            elif(value < reducedList[index]):
                self.compare(reducedList[0: index], value)
            else:
                print("found")
                return
    
    def check(self, testValue: int) -> str:
        if(testValue < self.orderedList[0] or testValue > self.orderedList[-1]):
            print("Out of bounds")
        else:
            self.compare(self.orderedList, testValue)


MyBin = BinSearch([1,2,4,5,6,7])

MyBin.check(3)

           
       



