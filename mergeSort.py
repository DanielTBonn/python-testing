import unittest


class TestSubArrays(unittest.TestCase):

    def __init__(self, array):
        self.array = array
    
    def test_equal(self):
        initial = self.array[0]
        subArray = self.array[1]
        self.assertEqual(initial, subArray)
    
    def test_notEqual(self):
        self.assertEqual([1,2], [1])

# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
def mergeSort(arr, l, r):
    
    
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
    else:
        test(arr, l, r)
 

def test(arr, l, r):
    l = 0
    r = len(arr) - 1
    if (arr[r] < 0 and arr[l] < abs(arr[r])):
        return []
    else:
        return arr
test([1, -2])



# Driver code to test above
# arr = [12, 11, 13, 5, 6, 7]
# arr = [-1, 2, -4, 5, -1, 6 -3, 2]
# arr = [1, -5 ,2, 3, -2, 4]
# arr = []
# greatestSum = sum(arr)
# n = len(arr)
# print("Given array is")
# for i in range(n):
#     print("%d" % arr[i],end=" ")
 
# answer = mergeSort(arr, 0, n-1, greatestSum)
# print('Answer: ',answer) 


x = 100

def foo(n, res):
    print(res)
    if (n == 0):
        return 1
    else:
        res = "hello world"
        return foo(n - 1, res)

foo(3, "python is weird")

# if __name__ == '__main__':
#     unittest.main([1,2])