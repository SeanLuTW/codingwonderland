"""
1089. Duplicate Zeros
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]


Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""

arr = [1,0,2,3,0,4,5,0]
#idea from disscussion
# i = 0       # it's better to start from the beginning as last elements will be removed
# while i < len(arr):     # while is better as the list will be modified
#     if arr[i] == 0:     # when element is 0
#         arr.insert(i, 0)        # insert 0 along to it
#         arr.pop()     # remove last element
#         i += 1      # go to the next element - after adding index has to be increased by 2
#     i += 1
# print (arr)

#discussion (can't not use extra space )
ans = []
for x in arr:
    if x == 0:
        ans.append(0)
    ans.append(x)
for i in range(len(arr)):
    arr[i] = ans[i]
print (ans[0:len(arr)])