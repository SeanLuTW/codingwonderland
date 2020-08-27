"""
Merge two sorted linked lists

Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order, and merges the two together into one list which is in increasing order. SortedMerge() should return the new list. The new list should be made by splicing
together the nodes of the first two lists.

For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20, then SortedMerge() should return a pointer to the head node of the merged list 2->3->5->10->15->20.

There are many cases to deal with: either ‘a’ or ‘b’ may be empty, during processing either ‘a’ or ‘b’ may run out first, and finally there’s the problem of starting the result list empty, and building it up while going through ‘a’ and ‘b’.
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
# Constructor to initialize the node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Method to print linked list 
    def printList(self): 
        temp = self.head 
          
        while temp : 
            print(temp.data, end="->") 
            temp = temp.next
  
    # Function to add of node at the end. 
    def append(self, new_data): 
        new_node = Node(new_data) 
          
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
          
        while last.next: 
            last = last.next
        last.next = new_node

def mergelist(head1,head2):
    #create a tmp node point to null
    tmp = None 
    #list1 is empty then return list2
    if head1 is None:
        return head2
    #list2 is empty then return list1
    if head2 is None:
        return head1
    # If List1's data is smaller or equal to List2's data
    if head1.data <=head2.data:
        #assign tmp to list1 's data
        tmp = head1
        # Again check List1's data is smaller or equal List2's  
        # data and call mergeLists function. 
        tmp.next = mergelist(head1.next,head2)
    else:
        # If List2's data is greater than or equal List1's  
        # data assign temp to head2 
        tmp = head2
        # Again check List2's data is greater or equal List's 
        # data and call mergeLists function. 
        tmp.next = mergelist(head1,head2.next)
    # return the temp list
    return tmp
# Driver Function 
if __name__ == '__main__': 
  
    # Create linked list : 
    # 10->20->30->40->50 
    list1 = LinkedList() 
    list1.append(10) 
    list1.append(20) 
    list1.append(30) 
    list1.append(40) 
    list1.append(50) 
  
    # Create linked list 2 : 
    # 5->15->18->35->60 
    list2 = LinkedList() 
    list2.append(5) 
    list2.append(15) 
    list2.append(18) 
    list2.append(35) 
    list2.append(60) 
    # Create linked list 3 
    list3 = LinkedList() 
  
    # Merging linked list 1 and linked list 2 
    # in linked list 3 
    list3.head = mergelist(list1.head, list2.head) 
  
    print(" Merged Linked List is : ", end="") 
    list3.printList()