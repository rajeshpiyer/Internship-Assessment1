#Matrix Multiplication

def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Matrix dimensions are not compatible for multiplication.")
        return None
    
    result = [[0 for a in range(len(matrix2[0]))] for a in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

def matrix_input():
    print("Enter the order of matrix : ")
    a=int(input("No of rows : "))
    b=int(input("No of Columns : "))

    matrix=[]
    for i in range(1,a+1):
        print("Row : ",i)
        sub_matrix=[]
        for j in range(1,b+1):
            item=int(input("Enter item "+str(j)+" : "))
            sub_matrix.append(item)
        matrix.append(sub_matrix)
    return matrix

print("First Matrix : ")
matrix1 = matrix_input()
print("Second Matrix : ")
matrix2 = matrix_input()

result = matrix_multiply(matrix1, matrix2)

print("\nMatrix 1 : \n")
for i in matrix1:
    print(i)
print("\nMatrix 2 : \n")
for i in matrix2:
    print(i)

if result:
    print("\nMatrix multiplication result:\n")
    for row in result:
        print(row)