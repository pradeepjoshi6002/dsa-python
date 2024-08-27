arr=['a','b','c','d','e','f','g','h','i']

def findPeak1(arr):
    
    for indx in range(len(arr)):
        if(indx==len(arr)-1):
            if(arr[indx]>=arr[indx-1] and indx>1):
                return indx
        elif(indx==0):
            if(arr[indx]>=arr[indx+1] and len(arr)>1):
                return indx
        elif(arr[indx]>=arr[indx-1] and arr[indx]>=arr[indx+1]):
            return indx
        
def findPeakBinary1(arr):
    s, e = 0, len(arr) - 1
    while s < e:
        mid = s + (e - s) // 2
        if mid > 0 and arr[mid] < arr[mid - 1]: 
            e = mid - 1
        elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]: 
            s = mid + 1
        else:  
            return mid
    return s
             
# print(arr[findPeak1(arr)])
# print(arr[findPeekBinary1(arr)])

# greedy ascent algorithm

# def greedyAscent(arr):
#     # only 2d arrays --> arr[][]
#     row,col=len(arr),len(arr[0])
#     argRow=row//2
#     while(row>0 and col>0):
#         peak=findPeekBinary1(arr[row//2])
#         if(arr[row//2][peak]<arr[row//2-1][peak]):
#             argRow=row//2-1
#         elif(arr[row//2][peak]<arr[row//2+1][peak]):
#             argRow=row//2+1
#         else:
#             return [row//2,peak]
        
def greedyAscent(arr):
    if not arr or not arr[0]:
        return None

    row, col = len(arr), len(arr[0])
    
    mid_row = row // 2

    while True:
        peak = findPeakBinary1(arr[mid_row])
        
        if mid_row > 0 and arr[mid_row][peak] < arr[mid_row - 1][peak]:
            mid_row -= 1
        elif mid_row < row - 1 and arr[mid_row][peak] < arr[mid_row + 1][peak]:
            mid_row += 1
        else:
            return [mid_row, peak]
