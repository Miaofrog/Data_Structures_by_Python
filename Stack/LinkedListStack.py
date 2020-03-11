#使用链表作为底层实现链栈
from LinkedList.LinkedList  import LinkedList
from Stack.StackInterface import StackInterface

class LinkedListStack(StackInterface):
    def __init__(self):
        self.__data = LinkedList()  #链表对象

    # 获取栈内元素个数
    def getSize(self):
        return self.__data.getSize()

    # 判断栈是否为空
    def isEmpty(self):
        return self.__data.isEmpty()

    # 入栈,在链表头插入
    def  push(self, e):
        self.__data.addFirst(e)

    #出栈，删除链表头元素
    def pop(self):
        self.__data.deleteFirst()

    #取栈顶元素
    def peek(self):
        return self.__data.getFirst()

    #打印输出链栈
    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return self.__str__()

#测试链栈操作
if __name__ == "__main__":
    linkedListStack = LinkedListStack()
    print(linkedListStack)

    linkedListStack.push("W")
    print(linkedListStack)

    linkedListStack.push("H")
    print(linkedListStack)

    linkedListStack.push("F")
    print(linkedListStack)

    linkedListStack.pop()
    print(linkedListStack)

