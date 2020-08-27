"""
609. Find Duplicate File in System

"""
"""
:type paths: List[str]
:rtype: List[List[str]]
"""
from collections import defaultdict
paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
dic = defaultdict(list)
for i in paths:
    tmp = i.split()
    # dic[tmp[0]] = tmp
    address = tmp[0]
    # print (address)#fd
    # print (tmp[1:])#fd
    for j in tmp[1:]:
        index = j.find("(")
        # print (index)#fd
        filename= j[:index]
        content = j[index:]
        dic[content].append(address + "/" + filename)
print (dic)
print ([dic[key] for key in dic if len(dic[key]) > 1])
print([dic[key] for key in dic if len(dic[key])>1])




#discussion ans
# paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

# import collections
# dic = collections.defaultdict(list)
# for path in paths:
#     p = path.split()
#     root = p[0]
#     for file in p[1:]:
#         idx = file.find("(")
#         fn, content = file[:idx], file[idx:]
#         dic[content].append(root + "/" + fn)
# print (dic)
# print ( [dic[key] for key in dic if len(dic[key]) > 1])