"""
811. Subdomain Visit Count

"""

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
#["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
from collections import Counter
ans = Counter()#dic type 
for i in cpdomains:
    num, domain = i.split()
    num = int(num)
    segment = domain.split('.')#list type 
    # print (segment)
    for j in range(len(segment)):#j would be string type
        print (segment[j:])#fd
        ans[".".join(segment[j:])] += num
        # ans[segment[j]]+=num
print(list(str(ans[i])+" "+i for i in ans))