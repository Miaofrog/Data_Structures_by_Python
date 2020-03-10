#使用动态数组底层实现循环队列
#注意：
#（1）不复用之前实现的动态数组，因为之前实现的动态数组没有front和tail
#（2）牺牲一个空间区分循环队列为空或满，开辟空间时要比用户传入的多一个
#（3）输出时要注意front和tail的位置

from Queue.QueueInterface import QueueInterface
from Queue.ArrayQueue import ArrayQueue
from time import time
from random import randint

class LoopQueue(QueueInterface):
    def __init__(self, capacity = 10):
        self.__data = [None] * (capacity + 1)   #默认空间大小为11的循环队列,牺牲一个空间
        self.__front = 0   #永远指向队首元素
        self.__tail = 0    #永远指向队尾待插入元素的位置
        self.__size = 0    #循环队列的元素个数

    #获取队列容量
    def getCapacity(self):
        return len(self.__data) - 1

    ## 获取队列内元素个数
    def getSize(self):
        return self.__size

    # 判断队列是否为空
    def isEmpty(self):
        return self.__front == self.__tail   #循环队列为空的条件

    #入队
    def enqueue(self, e):
        #判满扩容
        if (self.__tail + 1) % len(self.__data) == self.__front:
            # raise ValueError("循环队列已满！")
            self.__resize( self.getCapacity() * 2 )

        self.__data[self.__tail] = e   #将e插入tail位置
        self.__tail = (self.__tail + 1) % len(self.__data)   #维护tail
        self.__size += 1  #维护size

    #出队
    def dequeue(self):
        #判空
        if self.isEmpty():
            raise ValueError("循环队列为空！")

        ret = self.__data[self.__front]  #保存要删除元素返回

        self.__data[self.__front] = None   #删除元素
        self.__front = (self.__front + 1) % len(self.__data)  #维护front
        self.__size -= 1  #维护size

        # 如果元素较少可考虑缩小循环队列容量,防止复杂度震荡，等到capacity的1/4（不是1/2）时才缩容
        # 注意缩容的容量不能为0.当capacity = 1，size = 0满足size == capacity/4 ，但我们不再缩小数组容量
        if self.__size == self.getCapacity() // 4 and self.getCapacity() // 2 != 0:
            self.__resize(self.getCapacity() // 2)

        return ret

    def getFront(self):
        #判空
        if self.isEmpty():
            raise ValueError("循环队列为空")
        return self.__data[self.__front]

    #缩放循环队列容量
    def __resize(self, newCapacity):
        newData = [None] * (newCapacity + 1)  #牺牲一个空间
        #将data里元素全部复制到newdata里,
        for i in range(0, self.__size, 1):
            newData[i] = self.__data[ (self.__front + i) % len(self.__data) ]

        self.__data = newData
        self.__front = 0
        self.__tail = self.__size

    def __str__(self):
        #注意front和tail的位置前后
        if self.__tail >= self.__front:
            return "LoopQueue: front {} tail, size = {}, capacity = {}".format(self.__data[self.__front : self.__tail], self.__size, self.getCapacity())
        else:
            return "LoopQueue: front {} tail , size = {}, capacity = {}".format( str(self.__data[self.__front :] + self.__data[:self.__tail]),  self.__size, self.getCapacity())

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":

    # #测试循环队列的操作
    # loopQueue = LoopQueue()  # 创建顺序队列实例.初始为空
    # print(loopQueue)
    #
    # #测试入队操作
    # for i in range(0, 10, 1):
    #     loopQueue.enqueue(i)  #循环队列已满
    #     print(loopQueue)
    #
    # # 测试查询操作
    # print(loopQueue.getFront())
    #
    # # 测试出队操作
    # for i in range(0, 6):
    #     loopQueue.dequeue()  # 删掉5个，删除最后一个会缩容成8个空间
    #     print(loopQueue)
    #
    # # 再入队一个
    # loopQueue.enqueue("W")  # 循环队列已满
    # print(loopQueue)


    #比较顺序队列和循环队列的性能，主要是出队操作循环队列O(1),顺序队列O(n)
    def test_queue(queue, opCount):
        startTime = time()

        #先入队再出队
        for i in range(opCount):
            queue.enqueue(randint(1, 2000))
        for i in range(opCount):
            queue.dequeue()

        endTime = time()
        return endTime - startTime

    opCount = 10000

    arrayQueue= ArrayQueue()
    loopQueue = LoopQueue()

    time1 = test_queue(arrayQueue, opCount)
    time2 = test_queue(loopQueue, opCount)

    print("ArrayQueue: ", str(time1) + "s")  #ArrayQueue:  4.791930198669434s
    print("LoopQueue: ", str(time2) + "s")  #LoopQueue:  0.015619516372680664s





