#栈的接口,用于不同底层实现栈

class StackInterface(object):

    #获取栈内元素个数
    def getSize(self):
        raise NotImplementedError

    #判断栈是否为空
    def isEmpty(self):
        raise NotImplementedError

    #入栈
    def push(self, e):
        raise NotImplementedError

    #出栈
    def pop(self):
        raise NotImplementedError

    #取栈顶元素
    def peek(self):
        raise NotImplementedError
