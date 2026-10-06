

#array is m * n, in this case 4 * 4
A = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

#initial value of X
X = [0, 0, 0, 0]

#initial value of B
B = [1, 0, -1, 3]

#Recall AX = B

def populate_array(array):
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = 1/(i + j  + 1)

populate_array(A)


def gauss_siedel(A, X, B,  no_of_iterations):
    
    x1, x2, x3, x4 = X
    
    if no_of_iterations > 0:
        
        for _ in range(no_of_iterations):
            x1 = (B[0] - (A[0][1] * x2) - (A[0][2] * x3) - (A[0][3] * x4)) / A[0][0]
            x2 = (B[1] - (A[1][0] * x1) - (A[1][2] * x3) - (A[1][3] * x4)) / A[1][1]
            x3 = (B[2] - (A[2][0] * x1) - (A[2][1] * x2) - (A[2][3] * x4)) / A[2][2]
            x4 = (B[3] - (A[3][0] * x1) - (A[3][1] * x2) - (A[3][2] * x3)) / A[3][3]
            print(x1, x2, x3, x4)
    return [x1, x2, x3, x4]
                
gauss_siedel(A, X, B, 5)   