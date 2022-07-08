def insertion_sort(li):
    for i in range(1, len(li)):
        while li[i - 1] > li[i] and i > 0:
            li[i-1], li[i] = li[i], li[i-1]
            i -=1


li = [5, 3, 1, 4, 6, 9]
insertion_sort(li)
print(li)