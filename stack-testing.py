s = "   ]"

def checkS(s):
    dict1 = {'(' : ')', '{' : '}', '[' : ']'}
    # print(('(', '}') in dict1.items())

    stack = []
    for i in range(len(s)):
        if s[i] in "({[":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False 
            top = stack.pop()
            print(top, s[i])
            if ((top, s[i]) not in dict1.items()):
                return False
            
    if len(stack) > 0:
        return False
    
    return True

# print(checkS(s))

nums = [1,2,3,4]
# print(nums[1:len(nums)])

pointer1 = pointer2 = 3
pointer2 = len(nums)
testcase = [4, -5, 4, -2, 3, 1, -3, 5, -6, 5, -4]
print(sum(testcase[0:len(testcase)-3]))
print(pointer1, pointer2)

print(nums[:pointer2])
print(max(testcase))