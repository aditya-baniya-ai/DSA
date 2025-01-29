# for _ in range(any_number): means running the loop that number of times without using the index anywhere
# _ is just a filler
# we are doing [0]*3 that means [0][0][0] for 3 times, which will create a 3x3 matrix with 9 elements


def transpose(matrix):
    res = [[0]* len(matrix) for _ in range(len(matrix[0]))]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[j][i] = matrix[i][j]
            
    return res

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))