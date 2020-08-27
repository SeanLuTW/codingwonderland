"""
1233. Remove Sub-Folders from the Filesystem

Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

 

Example 1:

Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
Example 2:

Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are subfolders of "/a".
Example 3:

Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]
"""
"""
intuition:
sort by length then put only parent into Hashset(hashtable)

Sort cost n * logn;
Outer for loop run n times; inner for loop cost i in each iteration due to substring(0, i), that is, 2 + ... + m, which is O(m ^ 2);
Therefore,

Time: O(n * (logn + m ^ 2))
space: (n * m), where n = folder.length, m = average size of the strings in folder.


ref:
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409028/JavaPython-3-3-methods-from-O(n-*-(logn-%2B-m-2))-to-O(n-*-m)-w-brief-explanation-and-analysis.
"""
# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

check = set()
folder = sorted(folder,key = len)#sorted by len of element in folder list
# print (folder)
for i in folder:
    # print (i)
    for j in range(2,len(i)):
        if i[j] =='/' and i[:j] in check:
            break
    else:
        check.add(i)
print (list(check))