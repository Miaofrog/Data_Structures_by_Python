
#自己实现的数组类
class Array(object):

    def __init__(self, capacity=10):
        self.__data = [None] * capacity  #初始化有10个空间的数组
        self.__capacity = capacity   #数组可容纳的元素个数
        self.__size = 0    #初始数组中元素个数为0

    #获取数组已有元素个数
    def getSize(self):
        return self.__size

    #获取数组的容量
    def getCapacity(self):
        return self.__capacity

    #查看数组是否为空
    def isEmpty(self):
        return self.__size == 0  #返回布尔值

    #缩放数组容量
    def __resize(self, newCapacity):
        newData = [None] * newCapacity   #开辟新数组，容量为原来的2倍

        #将data中元素全部复制到newData中
        for i in range(0, self.__size, 1):
            newData[i] = self.__data[i]

        self.__data = newData
        self.__capacity = newCapacity

    #向数组中索引为index的位置添加元素e
    def add(self, index, e):
        #检查索引合法性
        if index < 0 or index > self.__size:
            raise ValueError("插入的位置不合法！")

        #判满，数组满了即扩容两倍
        if self.__size == self.__capacity:
            if self.__size == 0:
                self.__resize(1)  #数组为空只需要一个空间
            else:
                self.__resize(self.__capacity * 2)

        #将索引size-1~index的元素依次向后移一个位置，空出index位置
        for i in range(self.__size - 1, index - 1, -1):
            self.__data[i + 1] = self.__data[i]

        self.__data[index] = e   #将e插入index位置
        self.__size += 1   #元素个数加1

    # 向数组末尾添加元素e
    def addLast(self, e):
        self.add(self.__size, e)  #末尾索引就是size

    # 向数组头部添加元素e
    def addFirst(self, e):
        self.add(0, e)

    #获取index位置的元素
    def getElem(self, index):
        # 检查索引合法性
        if index < 0 or index > self.__size:
            raise ValueError("获取元素的位置不合法！")
        return self.__data[index]

    #获取第一个位置的元素
    def getFirst(self):
        return self.getElem(0)

    #获取最后一个位置的元素
    def getLast(self):
        return self.getElem(self.__size - 1)

    #修改数组中index位置的值
    def set(self,index, newValue):
        # 检查索引合法性
        if index < 0 or index > self.__size:
            raise ValueError("修改的位置不合法！")

        self.__data[index] = newValue


    #搜索元素e的位置
    def find(self, e):
        for i in range(0, self.__size, 1):
            if self.__data[i] == e:
                return i   #返回元素e的索引
        return -1 #遍历完还没找到就返回-1

    #查看数组中是否包含元素e
    def contains(self, e):
        index = self.find(e)
        if index != -1:
            return True
        return False

    #删除数组中index位置的元素，并返回
    def delete(self, index):
        # 检查索引合法性
        if index < 0 or index >= self.__size:
            raise ValueError("删除的位置不合法！")

        #不需要判空
        # 因为当size == 0时，index < 0 or index >= self.__size 恒成立

        #保存要删除的元素返回
        retElem = self.__data[index]

        #将inedx+1~size-1位置的元素依次向前移一个
        for i in range(index + 1, self.__size, 1):
            self.__data[i - 1] = self.__data[i]

        self.__data[self.__size - 1] = None
        self.__size -= 1  #元素个数减1

        #如果元素较少可考虑缩小数组容量,防止复杂度震荡，等到capacity的1/4（不是1/2）时才缩容
        # 注意缩容的容量不能为0.当capacity = 1，size = 0满足size == capacity/4 ，但我们不再缩小数组容量
        if self.__size == self.__capacity // 4 and self.__capacity // 2 != 0:
            self.__resize(self.__capacity // 2)

        return retElem

    #删除最后一个元素
    def deleteLast(self):
        return self.delete(self.__size - 1)

    #删除第一个元素
    def deleteFirst(self):
        return self.delete(0)
    
    
    #基于数组实现最大堆时要使用到交换两个位置的元素
    def swap(self, i, j):
        self.__data[i], self.__data[j] = self.__data[j], self.__data[i]
        

    #打印输出
    def __str__(self):
        return "Array: {}, size = {}, capacity = {}".format(self.__data, self.__size, self.__capacity)

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    arr = Array()   #创建数字实例
    print(arr)

    #测试插入操作
    for i in range(0, 10, 1):
        arr.addLast(i)
    print(arr)

    #测试查询操作
    print(arr.getElem(4))
    print(arr.getFirst())

    #测试扩容操作
    arr.add(3, "W")  #或扩容
    print(arr)

    #测试删除操作
    for i in range(0, 5):
        arr.deleteLast()   #删掉5个
    print(arr)

    #测试缩容操作
    arr.deleteLast()
    print(arr)
