###创建大规模数据的数组，用于测试各种排序算法的性能
import random
from random import randint
from time import time
from Array.Array import Array

#产生随机数组，范围在range_L, range_R之间
def generate_random_array(n, range_L, range_R):
    random.seed(time())
    array = Array()
    for i in range(0, n, 1):
        array.addLast(randint(range_L, range_R))
    return array

#产生随机列表，范围在range_L, range_R之间
def generate_random_list(n, range_L, range_R):
    random.seed(time())
    arr = [randint(range_L, range_R) for i in range(0, n, 1) ]
    return arr

#产生几乎有序的列表
def generate_nearly_ordered_random_list(n, swap_times):
    random.seed(time())
    arr = [i for i in range(0, n, 1)]  #完全有序列表，从小到达
    for swap_time in range(0,swap_times,1):
        i = randint(0, n-1)
        j = randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]  #随机交换两个位置的元素
    return arr



#测试函数，计算某个排序函数执行的时间
def test_sort(sort_name, sort_func, arr):
    startTime = time()
    sort_func(arr)
    endTime = time()
    print("algorithm = {}".format(sort_name))
    print("time = {}".format(endTime - startTime) + "s")
    assert is_sorted(arr)


#测试是否从小到大排序正确
def is_sorted(arr):
    for i in range(0, len(arr)-1, 1):
        if arr[i] > arr[i+1]:
            return False
    return True




def union_find_test_helper(uf, n, uf_name):
    pass