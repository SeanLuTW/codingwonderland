"""
1108. Defanging an IP Address

iven a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

"""
address = "255.100.50.0"
#approach 1 
# print (address.replace(".","[.]"))

#approach 2 
# a = address.split('.')
# print (a)
# b = '[.]'.join(a)
# print (b)

#approach 3 one liner 

print ('[.]'.join(address.split('.')))
