class MergeSort:
        
    def sort(self, array):
        if(len(array) > 1):
            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]
            self.sort(left)
            self.sort(right)
            
            l = 0
            r = 0
            c = 0
            
            while(l < len(left) and r < len(right)):
                if(left[l] < right[r]):
                    array[c] = left[l]
                    c += 1
                    l += 1
                else:
                    array[c] = right[r]
                    c += 1
                    r += 1
                
            while(l < len(left)):
                array[c] = left[l]
                c += 1
                l += 1
            
            while(r < len(right)):
                array[c] = right[r]
                c += 1
                r += 1
                
            print(array)
                
                
        
    

myMergeSort = MergeSort()

myMergeSort.sort([20, 5, 4])

