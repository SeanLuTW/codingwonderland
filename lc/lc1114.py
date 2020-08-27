"""
1114. Print in Order

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

 

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
"""

"""
intuition :
idea from discussion 
"""
from threading import Lock
class Foo:

    def __init__(self):
        self.lock1 = Lock()#create lock
        self.lock2 = Lock()#create lock
        self.lock1.acquire()#get the lock1
        self.lock2.acquire()#get the lock2


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()#release lock1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()#wait for first finished,after relase lock1 then able to use lock1
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock2.release()#release lock2

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock2.acquire()# wait for second finished
        # printThird() outputs "third". Do not change or remove this line.
        printThird()