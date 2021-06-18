
"""
   Given a 2-D square matrix A[n,n] and it is known that the values along each row and each column 
   are sorted in ascending order. Write an efficient program to search for the location of query
   value q in A: if q is in A, then return the position (i, j); otherwise returns -1.
"""

"""
design idea:
treat the matrix as flat list and then perform binary search
in the binary search we have to define left and right
also, we have to define the middle index for the matrix 
For the matrix we have 2 dimention, so we can
have to make sure the middle index is in the middle of the matrix
Last, we will just perform binary search to get the index of the target 
"""
def matrix_binary_search(target,A):
   if not A: #return -1 if matrix A is empty 
      return -1
   elif A[0][0] == target: #return index if the target is in the first position
      return [0,0]
   length = len(A[0])
   left, right = 0, ((length * len(A)) - 1) #set the left most and right most - 1
   
   while left <= right:
      mid = (left + right) // 2 # treat it as flat arrary and get the middle index of the matrix 
      row,col = mid // length, mid % length # get the middle index of the matrix

      if A[row][col] == target: # return index if the target is found
            return[row,col]
      elif A[row][col] < target: # if the current element  is less than the taget, move left indedx to the right
            left = mid + 1
      else:
         right = mid - 1 # else move right index to the left
   return -1 


A = [
[1,2,3],
[4,5,6],
[7,8,9]]
B = [
[1,2,3,3],
[4,5,6,6],
[7,8,9,9]]
target = 6
result = matrix_binary_search(target,B)
print(result)

