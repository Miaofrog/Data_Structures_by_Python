#使用动态数组底层实现顺序栈
from Stack.StackInterface import StackInterface
from Array.Array import Array


class ArrayStack(StackInterface):

    def __init__(self, capacity=0):
        # 动态数组对象, 容量默认为10，有10个空间的顺序栈，
        # 用户可自定义栈的大小
        self.__data = Array(capacity)
        # self.__size = 0  不需要维护size，下面用不到


    # 获取栈内元素个数
    def getSize(self):
        return self.__data.getSize()

    # 判断栈是否为空
    def isEmpty(self):
        return self.__data.isEmpty()

    # 入栈
    def push(self, e):
        self.__data.addLast(e)

    # 出栈
    def pop(self):
        return self.__data.deleteLast()

    # 取栈顶元素
    def peek(self):
        return self.__data.getLast()

    def __str__(self):
        return "ArrayStack:{}, size = {}".format(self.__data, self.__data.getSize())

    def __repr__(self):
        return self.__str__()

#括号匹配
if __name__ == "__main__":

    #(1)可能的测试用例（正面和负面）
    string1 = "()[]{}"   #True
    string2 = "([])"     #True
    string3 = ""       #空字符串True
    string4 = "([{)]}"   #False
    string5 = "(abc)"  #包含其他字符串False
    string6 = "(){}["  #元素个数为奇数

    #(2)匹配函数
    def is_valid(string):

        #空字符串
        if len(string) == 0:
            return True

        #字符串长度为奇数
        if len(string) % 2 != 0:
            return False

        arrayStack = ArrayStack()  # 顺序栈实例
        for char in string:
            if char == "(" or char == "[" or char == "{":
                arrayStack.push(char)
            elif char == ")" or char == "]" or char == "}":
                #char与栈顶元素进行匹配,但栈顶元素可能没有
                if arrayStack.isEmpty():
                    return False

                topChar = arrayStack.peek()
                if char == ")" and topChar == "(":
                    arrayStack.pop()
                elif char == "]" and topChar == "[":
                    arrayStack.pop()
                elif char == "}" and topChar == "{":
                    arrayStack.pop()
                else:
                    return False
            else: #有其他字符
                return False

        #看栈是否为空
        if not arrayStack.isEmpty():
            return False
        return True


    #(3)测试输出
    print(is_valid(string1))
    print(is_valid(string2))
    print(is_valid(string3))
    print(is_valid(string4))
    print(is_valid(string5))
    print(is_valid(string6))

