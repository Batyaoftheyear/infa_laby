def insertion_sort(alist):
    for i in range(1, len(a_list)):
        temp = a_list[i]
        j = i - 1
        while (j >= 0 and temp < a_list[j]):
            a_list[j + 1] = a_list[j]
            j = j - 1
        a_list[j + 1] = temp
a_list = input().split()
a_list = [int(x) for x in a_list]
insertion_sort(a_list)
print(alist)
