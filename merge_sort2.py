# -*- coding: UTF-8 -*-
# 归并排序算法demo 2


def merge_sort(arr):

    def merge(left, right):
        temp = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                temp.append(left.pop(0))
            else:
                temp.append(right.pop(0))

        temp += left
        temp += right
        return temp

    if len(arr) == 1:
        return arr

    # 取拆分的中间位置
    mid = len(arr) // 2
    # 拆分过后左右两侧子串
    left = arr[:mid]
    right = arr[mid:]
    x = merge_sort(left)
    y = merge_sort(right)
    return merge(x, y)


x = merge_sort([4, 3, 2, 1])
print(x)
