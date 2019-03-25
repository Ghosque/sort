
def insert_sort(alist):
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果比前面的小就交换
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j-1], alist[j] = alist[j], alist[j-1]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(alist)
print(alist)

