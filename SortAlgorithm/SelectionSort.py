from Sort_Test_Helper.Helpers import generate_random_list
from Sort_Test_Helper.Helpers import test_sort

###选择排序
def selectionSort(arr):
    for i in range(0, len(arr), 1):
        ###找arr[i...n)之间的最小值
        minIndex = i  #默认第一个元素最小
        for j in range(i+1, len(arr), 1):
            if arr[j] < arr[minIndex]:
                minIndex = j

        ###找到了最小值的索引，与arr的此时的第一个位置交换
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

###选择排序时间复杂度O(n^2)
if __name__ == "__main__":
    n = 10000

    arr = generate_random_list(n, 0, n)
    test_sort("SelectionSort", selectionSort, arr)

    ##n=10000  time = 2.5s    O(n^2)
    ##n=20000  time = 10.3s   O(4n^2)



