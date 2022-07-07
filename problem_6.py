# this is the list to count the minimum swap of this list
num_list = [1, 5, 4, 3, 2, 10, 6, 7, 9]
# this  is function will help to count the number of swaps
def minmum_Swaps(num_list):
    s = len(num_list)
    counter = [*enumerate(num_list)]
    counter.sort(key=lambda it: it[1])
    skip = {k: False for k in range(s)}
    result = 0
    for i in range(s):
        if skip[i] or counter[i][0] == i:
            continue
        size = 0
        h = i
        while not skip[h]:
            skip[h] = True
            h = counter[h][0]
            size += 1
        if size > 0:
            result += (size - 1)
    return result
print("the minimum swaps are:", minmum_Swaps(num_list))
