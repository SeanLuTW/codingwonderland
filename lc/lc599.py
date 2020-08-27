"""
599. Minimum Index Sum of Two Lists

"""
"""
Suppose Andy and Doris want to choose a restaurant for dinner, 
and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
 If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """


# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]

love = set(list1) & set(list2)
# print(love)

#find out least index sum string
anslist = []
sumdic = {}
for i in love:

    total = list1.index(i) + list2.index(i)
    sumdic[i] = total
ans = min(sumdic, key=sumdic.get)
anslist.append(ans)
print (anslist)
