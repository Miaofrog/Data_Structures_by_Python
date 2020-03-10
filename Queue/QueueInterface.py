#队列的接口，用于不同底层实现

class QueueInterface(object):

    # 获取队列内元素个数
    def getSize(self):
        raise NotImplementedError

    # 判断队列是否为空
    def isEmpty(self):
        raise NotImplementedError

    #入队
    def enqueue(self, e):
        raise NotImplementedError

    #出队
    def dequeue(self):
        raise NotImplementedError

    #取队首元素
    def getFront(self):
        raise NotImplementedError