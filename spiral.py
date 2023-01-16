'''
Have the function MatrixSpiral(strArr) read the array of strings stored in strArr which will represent a 2D N matrix, and your program should return the elements after printing them in a clockwise, spiral order. You should return the newly formed list of elements as a string with the numbers separated by commas. For example: if strArr is "[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]" then this looks like the following 2D matrix:

1 2 3
4 5 6
7 8 9

So your program should return the elements of this matrix in a clockwise, spiral order which is: 1,2,3,6,9,8,7,4,5
Examples
Input: ["[1, 2]", "[10, 14]"]
Output: 1,2,14,10
Input: ["[4, 5, 6, 5]", "[1, 1, 2, 2]", "[5, 4, 2, 9]"]
Output: 4,5,6,5,2,9,2,4,5,1,1,2
'''
import ast
def MatrixSpiral(strArr): 
    a=len(strArr)
    b=[]
    for i in range(a):
        k=ast.literal_eval(strArr[i])
        b.append(k)
    strArr=b
    z=[]
    i=0 #filas
    j=0#columnas
    m=len(strArr) #filas
    n=len(strArr[0]) #columna
    c=m*n
    while (i<=(m))&(j<=(n)):
        for l in range(i,n):
            z.append(strArr[i][l])
        i+=1
        if len(z)==c:
            break
    
        for l in range(i,m):
            z.append(strArr[l][n-1])
        for l in range(j,n-1):
            z.append(strArr[m-1][n-2-l])
        for l in range(i,m-1):
            z.append(strArr[m-1-l][j])
        n-=1
        m-=1
        j+=1
    s=[str(z) for z in z]
    s=",".join(s)
    return(s)
# keep this function call here  
print(MatrixSpiral(input()))


'''def spiral(matrix):
	spiral_array=[]
	for row in range(len(matrix)):
		if row%2==0:
			spiral_array.extend(matrix[row])
		else:
			matrix[row].reverse()
			spiral_array.extend(matrix[row])
	return spiral_array 

print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
'''