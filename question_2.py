
"""
   For an integer array A of n+1 numbers that are already sorted in ascending order, 
   one unknown number is repeated and put next to it, e.g., for n=5, A is [1,2,2,3,4,5], 2 is repeated.
   Write an efficient program of time complexity O(log n) to find out which number is repeated.
"""
"""
design idea
we use bineary seach to find the repeated number
we can set a right and left begin with 0 and length of arrary A - 1 (in case of out of index)
we start to check if the middle index of array A is the repeating value
then if A[mid] is equal to A[mid - 1] then we can just return the value
otherwise we will adjust the left and right index 

"""
def find_duplicate(left, right, A):
   if left > right: # if A is a empty array of reach to the end
      return -1
   mid = (left + right) // 2 # go to middle of the array
   if A[mid] != mid + 1: # check if the middle index is equal to middle index - 1
      if mid > 0  and A[mid] == A[mid - 1]:
         return A[mid] # return the value if it is repeating element
      return find_duplicate(left,mid - 1, A) # if not it means the we have to move right index to left 
      # so we move the right index to be mid - 1
   return find_duplicate(left + 1,right,A) # if right index is in right position then we have to move left index to right


   

A= [1,2,2,3,4,5]
A2=[1,2,3,3,4,5]
A3 = [1,2,3,4,4,4,5]
result = find_duplicate(0,len(A) - 1,A) #start from the left-most and right-most - 1
print(result)
result = find_duplicate(0,len(A2) - 1,A2)
print(result)
result = find_duplicate(0,len(A3) - 1,A3)
print(result)

