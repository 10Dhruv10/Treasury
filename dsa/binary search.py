# binary search on answer

def helper(arr, n):
    low, high = min(arr), max(arr)

    while low <= high:
        mid = (low+high)//2

        if predicate(mid)