#底层实现链表基础

class LinkedList(object):

    #内部链表节点类
    class __Node(object):
        #初始化一个节点，用户可传入元素和next，默认为空
        def __init__(self, e=None, next=None):
            self.e = e
            self.next = next

        #打印节点元素值
        def __str__(self):
            return str(self.e)

        def __repr__(self):
            return self.__str__()

    #初始化一个链表，不带虚拟头结点，以后不再用不带虚拟头结点的初始化
    # def __init__(self):
    #     self.__head = None  #第一个元素节点为空
    #     self.__size = 0

    # 初始化一个链表，带虚拟头结点
    def __init__(self):
        self.__dummyhead = self.__Node()  #虚拟头结点，初始next为空
        self.__size = 0
        
    #传入一个列表，返回一个链表,元素正序
    def listToLinkedList(self, list):
        if list is None or len(list) == 0:
            raise ValueError("列表为空，无法构造链表！")

        #尾插法构建链表
        cur = self.__dummyhead
        for i in range(0, len(list)):
            newNode = self.__Node(list[i])
            cur.next = newNode
            cur = cur.next
            self.__size += 1

        return self.__dummyhead.next

    #获取链表元素个数
    def getSize(self):
        return self.__size

    #判断链表是否为空
    def isEmpty(self):
        return self.__size == 0

    def add(self, index, e):
        # 首先检查index合法性
        if index < 0 or index > self.__size:
            raise ValueError("插入的索引不正确！")

        #不需要对第一个元素节点进行特殊处理
        #先找到插入位置的前一个位置
        prev = self.__dummyhead
        for i in range(0, index, 1): #从虚拟头结点开始prev移动index次
            prev = prev.next

        #找到prev之后就插入
        newNode = self.__Node(e)
        newNode.next = prev.next
        prev.next = newNode

        self.__size += 1

    def addFirst(self, e):
        self.add(0, e)

    def addLast(self, e):
        self.add(self.__size, e)

    # 删除虚拟头结点链表中index索引的元素并返回
    def delete(self, index):
        # 检查index的合法性,删除时不能等于size
        if index < 0 or index >= self.__size:
            raise ValueError("删除的索引不正确！")

        # 找到index位置的前一个位置
        prev = self.__dummyhead
        for i in range(0, index, 1):  # prev移动index次
            prev = prev.next

        delNode = prev.next  # 保存要删除的节点
        prev.next = delNode.next
        delNode.next = None
        self.__size -= 1

        return delNode.e

    def deleteFirst(self):
        return self.delete(0)

    def deleteLast(self):
        return self.delete(self.__size - 1)
    
    # 删除虚拟头结点链表中指定元素，其实只删除了指定元素第一次出现的位置
    def deleteElem(self, e):
        # 找到这个元素的前一个位置
        prev = self.__dummyhead
        while prev.next is not None:
            if prev.next.e == e:
                break
            prev = prev.next

        if prev.next is not None:  # 有元素e而不是遍历结束
            # 删除元素e
            delNode = prev.next  # 保存要删除的节点
            prev.next = delNode.next
            delNode.next = None
            self.__size -= 1

    # 删除虚拟头结点链表中指定元素的所有结点
    def deleteAllElem(self, elem):
        #遍历链表
        prev = self.__dummyhead
        while prev.next is not None:
            if prev.next.e == elem:  #找到就删除一个
                delNode = prev.next  # 保存要删除的节点
                prev.next = delNode.next
                delNode.next = None
                self.__size -= 1
            else:
                prev = prev.next

    #查询链表中某个位置上的元素
    def get(self, index):
        # 检查index的合法性,查询时不能等于size
        if index < 0 or index >= self.__size:
            raise ValueError("查询的索引不正确！")

        #找到index位置
        cur = self.__dummyhead.next
        for i in range(0, index, 1):  # cur移动index次
            cur = cur.next
        return cur.e

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.__size - 1)

    #更新链表中某个位置的元素
    def set(self, index, newElem):
        # 检查index的合法性,查询时不能等于size
        if index < 0 or index >= self.__size:
            raise ValueError("更新的索引不正确！")
        # 找到index位置
        cur = self.__dummyhead.next
        for i in range(0, index, 1):
            cur = cur.next
        cur.e = newElem

    #查询链表中是否有元素e
    def contains(self, e):
        prev = self.__dummyhead
        while prev.next is not None:
            if prev.next.e == e:
                return True
            prev = prev.next
        return False


    #打印输出链表
    def __str__(self):
        res = []
        cur = self.__dummyhead
        while cur.next is not None:
            res.append(str(cur.next.e))
            cur = cur.next
        return "LinkedList: Head "+ "-->".join(res) + " tail"

    def __repr__(self):
        return self.__str__()

#测试链表功能
if __name__ == "__main__":
    linkedList = LinkedList()
    print(linkedList)

    #头插法构造链表
    for i in range(0, 5, 1):
        linkedList.addFirst(i)
        print(linkedList)

    for i in range(0, 3):
        linkedList.deleteFirst()
        print(linkedList)
