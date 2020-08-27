"""
1184. Distance Between Bus Stops

"""

distance = [7,10,1,12,11,14,5,0]
start = 7
destination = 2


#idea from discussion 
"""
calculating clockwise and couter clock and get the min
"""
a = min(start, destination)
print (a)
b = max(start, destination)
print (b)
clockwise = sum(distance[a:b])
couterwise = sum(distance) - sum(distance[a:b])
print (clockwise)
print(couterwise)
print (min(sum(distance[a:b]), sum(distance) - sum(distance[a:b])))

