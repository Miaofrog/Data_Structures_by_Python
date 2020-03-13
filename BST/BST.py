#底层实现二分搜索树（二叉排序树）

class BST(object):

    #定义内部结点类：
    class __Node(object):
        def __init__(self, e=None, left=None, right=None):
            self.e = e
            self.left = left
            self.right = right

        def __str__(self):
            return str(self.e)

        def __repr__(self):
            return self.__str__()

    #BST的初始化
    def __init__(self):
        self.__root = None
        self.__size = 0

    #获取BST中节点个数
    def getSize(self):
        return self.__size

    #判断BST是否为空
    def isEmpty(self):
        return self.__size == 0


    #向BST中添加元素：非递归写法,以后基本不用
    def addNR(self, e):
        if self.isEmpty():
            self.__root = self.__Node(e)
            self.__size += 1
            return self.__root

        #BST不空,依次进行比较,插入节点肯定是叶子节点
        prev = self.__root
        #寻找e的父亲结点
        while prev.left is not None and prev.right is not None:
            if e < prev.e:
                prev = prev.left
            elif e > prev.e:
                prev = prev.right
            else:
                return

        #找到了插入的前一个结点prev,但是还不知道是插入右边还是左边
        newNode = self.__Node(e)
        if e < prev.e:
            prev.left = newNode
            self.__size += 1
        elif e > prev.e:
            prev.right = newNode
            self.__size += 1




    #用户角度：向BST中添加元素,参数为e
    def add(self, e):
        self.__root = self.__add(self.__root, e)

    #开发者角度：向BST中添加元素：递归写法
    def __add(self, node, e):
        #递归终止条件
        if node == None:
            self.__size += 1
            return self.__Node(e)  #返回新元素结点给上一层

        #未到终止条件时
        if e < node.e:
            node.left = self.__add(node.left, e)
        elif e > node.e:
            node.right = self.__add(node.right, e)
        #等于不做处理
        return node



    #用户：查询BST中是否包含某元素
    def contains(self,e):
        return self.__contains(self.__root, e)

    #开发者：查询询BST中是否包含某元素,递归解法
    def __contains(self, node, e):
        #递归终止条件
        if node == None:
            return False

        #未到终止条件时
        if e == node.e:
            return True
        elif e < node.e:
            return self.__contains(node.left, e)
        else:#e > node.e
            return self.__contains(node.right, e)



    #用户：前序遍历BST
    def preOrder(self):
        self.__preOrder(self.__root)
    #开发者：前序遍历BST，递归实现
    def __preOrder(self, node):
        if node == None:
            return

        print(node.e)  #遍历想要做的操作，先访问根结点
        self.__preOrder(node.left)
        self.__preOrder(node.right)

    #前序遍历BST，非递归实现，借助python列表替代栈来实现（深度优先遍历）
    def preOrderNR(self):
        if self.__root == None:
            return

        stack = [] #初始化栈
        stack.append(self.__root)
        while len(stack) != 0:
            topNode = stack.pop(-1)
            print(topNode.e)
            if topNode.right is not None:
                stack.append(topNode.right)
            if topNode.left is not None:
                stack.append(topNode.left)



    # 用户：中序遍历BST
    def inOrder(self):
        self.__inOrder(self.__root)
    # 开发者：中序遍历BST，递归实现
    def __inOrder(self, node):
        if node == None:
            return

        self.__inOrder(node.left)
        print(node.e)  # 遍历想要做的操作，先访问根结点
        self.__inOrder(node.right)



    # 用户：后序遍历BST
    def postOrder(self):
        self.__postOrder(self.__root)
    # 开发者：后序遍历BST，递归实现
    def __postOrder(self, node):
        if node == None:
            return

        self.__postOrder(node.left)
        self.__postOrder(node.right)
        print(node.e)  # 遍历想要做的操作，先访问根结点



    #层次遍历BST，非递归写法，借助列表替代队列（广度优先遍历）
    def levelOrder(self):
        if self.__root == None:
            return

        queue = []   #列表替代队列
        queue.append(self.__root)
        while len(queue) != 0:
            topNode = queue.pop(0)  #队首元素出队
            print(topNode.e)
            if topNode.left is not None:
                queue.append(topNode.left)
            if topNode.right is not None:
                queue.append(topNode.right)


    #用户：求BST的最小值结点，返回最小值结点
    def findMin(self):
        if self.isEmpty():
            raise ValueError("BST is empty!")
        return self.__findMin(self.__root)

    #开发者：递归求BST的最小值结点，返回最小值结点
    def __findMin(self, node):
        #递归终止条件
        if node.left == None:
            return node

        #递归未终止时
        return self.__findMin(node.left)



    #用户：求BST的最大值结点，返回最大值结点
    def findMax(self):
        if self.isEmpty():
            raise ValueError("BST is empty!")
        return self.__findMax(self.__root)

    #开发者：递归求BST的最大值结点，返回最大值结点
    def __findMax(self, node):
        # 递归终止条件
        if node.right == None:
            return node

        # 递归未终止时
        return self.__findMax(node.right)



    #用户：删除BST中最小值结点,返回最小值结点的值
    def deleteMin(self):
        minNode = self.findMin()
        self.__root = self.__deleteMin(self.__root)  #删除掉最小值结点的BST
        return minNode.e

    #开发者：递归删除BST中最小值结点，并返回值
    def __deleteMin(self, node):
        #递归终止条件
        if node.left == None:
            rightNode = node.right  #保存右子树，返回给父节点的左孩子
            node.right = None
            self.__size -= 1
            return rightNode

        #未到终止条件时
        node.left = self.__deleteMin(node.left)
        return node



    # 用户：删除BST中最大值结点,返回最大值结点的值
    def deleteMax(self):
        maxNode = self.findMax()
        self.__root = self.__deleteMax(self.__root)  # 删除掉最小值结点的BST
        return maxNode.e

    # 开发者：递归删除BST中最小值结点，并返回值
    def __deleteMax(self, node):
        # 递归终止条件
        if node.right == None:
            leftNode = node.left  # 保存左子树，返回给父节点的右孩子
            node.left = None
            self.__size -= 1
            return leftNode

        # 未到终止条件时
        node.right = self.__deleteMax(node.right)
        return node




    #用户：删除BST中任意一个值为e的元素结点
    def delete(self, e):
        if self.isEmpty():
            raise ValueError("BST is empty!")
        self.__root = self.__delete(self.__root, e)

    #开发者角度：递归实现删除BST中值为e元素结点并返回
    def __delete(self, node, e):
        #递归终止条件：
        if node == None: #没找到元素e结点
            return

        #未到递归终止条件时
        if e < node.e:
            node.left = self.__delete(node.left, e)
            return node
        elif e > node.e:
            node.right = self.__delete(node.right, e)
            return node
        else: #e == node.e 找到了元素e结点，接下来要看e有没有左右子树
            if node.left is None:
                rightNode = node.right
                node.right = None
                self.__size -= 1
                return rightNode

            if node.right is None:
                leftNode = node.left  # 保存左子树，返回给父节点的右孩子
                node.left = None
                self.__size -= 1
                return leftNode

            # 最复杂的情况，删除结点左右子树均有
            # 找到比待删除结点大的最小结点，即待删除右子树的最小值结点
            # 用这个结点替代删除节点的位置
            houjiNode = self.__findMin(node.right)
            houjiNode.right = self.__deleteMin(node.right)
            houjiNode.left = node.left
            node.left = node.right = None
            #不需要size-1，因为删除掉了后继结点
            return houjiNode

            #或者使用前驱结点,即待删除左子树的最大值结点
            # qianquNode = self.__findMax(node.left)
            # qianquNode.left = self.__deleteMax(node.left)
            # qianquNode.right = node.right
            # node.left = node.right = None
            # return qianquNode



    #怎么打印输出树的结构,以——的长度来表示深度
    def __generateDepthString(self, depth):
        res = ""
        for i in range(0, depth, 1):
            res = res + "—— "  #——的个数就代表深度
        return res

    def __generateBSTString(self, node, depth, res):
        #递归终止条件
        if node == None:
            res.append(self.__generateDepthString(depth) + "None\n")  #这一层是空的
            return

        #未到终止条件时
        res.append(self.__generateDepthString(depth) + str(node.e) + "\n")
        self.__generateBSTString(node.left, depth + 1, res)
        self.__generateBSTString(node.right, depth + 1, res)

    def __str__(self):
        res = []
        self.__generateBSTString(self.__root, 0, res)
        return "BST: " + " ".join(res)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    bst = BST()

    #测试添加功能
    nums = [5,3,6,8,4,2,2,2]
    for num in nums:
        bst.add(num)
        # bst.addNR(num)  #非递归添加
    print(bst)

    #测试前中后序遍历
    bst.preOrder()
    print("----------")
    bst.preOrderNR()
    print("----------")
    bst.inOrder()
    print("----------")
    bst.postOrder()
    print("----------")
    bst.levelOrder()

    #测试查询功能
    print(bst.findMin())
    print(bst.findMax())

    #测试删除功能
    bst.deleteMin()
    print(bst)
    bst.deleteMax()
    print(bst)
    bst.delete(5)
    print(bst)




