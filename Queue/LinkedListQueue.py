#基于链表实现链队列
#注意：我们不复用已经实现的链表，因为队列还有其他初始值
from Queue.QueueInterface import QueueInterface

class LinkedListQueue(QueueInterface):

    #内部节点类，用户可传入e和next
    class __Node(object):
        def __init__(self, e=None, next=None):
            self.e = e
            self.next = next

        def __str__(self):
            return str(self.e)

        def __repr__(self):
            return self.__str__()

    #链队列初始化，带虚拟头结点
    def __init__(self):
        self.__dummyhead = self.__Node()  #虚拟头结点
        self.__tail = self.__dummyhead   #永远指向最后一个元素
        self.__size = 0

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    #入队，在队尾入队
    def enqueue(self, e):
        newNode = self.__Node(e)
        self.__tail.next = newNode
        self.__tail = self.__tail.next  #维护tail

        self.__size += 1  #维护size

    #出队，在队首出队
    def dequeue(self):
        if self.isEmpty():
            raise ValueError("队列为空不能再删除！")

        delNode = self.__dummyhead.next
        self.__dummyhead.next = delNode.next
        delNode.next = None

        self.__size -= 1
        #一般删除不用维护tail，但是如果删除的是tail指向的节点就要考虑
        if self.__size == 0:
            self.__tail = self.__dummyhead

        return delNode.e

    #获取队首元素
    def getFront(self):
        if self.isEmpty():
            raise ValueError("队列为空！")

        return self.__dummyhead.next.e

    def __str__(self):
        data = []
        cur = self.__dummyhead
        while cur.next is not None:
            data.append(str(cur.next.e))
            cur = cur.next
        return "LinkedListQueue: Head " + "-->".join(data) + " tail"

    def __repr__(self):
        return self.__str__()

#测试链队列操作
if __name__ == '__main__':
    queue = LinkedListQueue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(100)
    queue.enqueue(9)
    print(queue)

    queue.dequeue()
    print(queue)

    queue.enqueue('zhe')
    print(queue)

    queue.dequeue()
    print(queue)