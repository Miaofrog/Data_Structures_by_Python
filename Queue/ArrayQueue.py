#使用动态数组实现顺序队列
from Queue.QueueInterface import QueueInterface
from Array.Array import Array

class ArrayQueue(QueueInterface):

    def __init__(self, capacity=0):
        # 动态数组对象, 容量默认为10，有10个空间的顺序队列，
        # 用户可自定义队列的大小
        self.__data = Array(capacity)

    # 获取队列内元素个数
    def getSize(self):
        return self.__data.getSize()

    # 判断队列是否为空
    def isEmpty(self):
        return self.__data.isEmpty()

    # 入队
    def enqueue(self, e):
        self.__data.addLast(e)

    #出队
    def dequeue(self):
        return self.__data.deleteFirst()

    # 取队首元素
    def getFront(self):
        return self.__data.getFirst()

    def __str__(self):
        return "ArrayQueue: {}".format(self.__data)

    def __repr__(self):
        return self.__str__()


#测试顺序队列的功能
if __name__ == "__main__":
    arrayQueue = ArrayQueue()  # 创建顺序队列实例
    print(arrayQueue)

    #测试入队操作
    for i in range(0, 10, 1):
        arrayQueue.enqueue(i)  # 会不停扩容，增加最后一个元素会扩容成16个空间
        print(arrayQueue)
    #
    # 测试查询操作
    print(arrayQueue.getFront())

    # 测试出队操作
    for i in range(0, 6):
        arrayQueue.dequeue()  # 删掉5个，删除最后一个会缩容成8个空间
        print(arrayQueue)
