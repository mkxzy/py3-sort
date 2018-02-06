# -*- coding: UTF-8 -*-
# 冒泡排序算法demo


def bubble_sort(arr):
    '''冒泡排序算法
    '''
    length = len(arr)
    for x in range(length):
        for y in range(length-1-x):
            if(arr[y] > arr[y+1]):
                arr[y], arr[y+1] = arr[y+1], arr[y]


data = [9, 5, 1, 8]
bubble_sort(data)
print(data)
print(bubble_sort.__doc__)
