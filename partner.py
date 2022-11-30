# must be in-place sort
def quick_sort(arr,cmp):
    if len(arr) > 1:
        # partition array
        pivot = arr[0]
        left = []
        right = []

        for x in range(1, len(arr)):
            c = cmp(arr[x], pivot)
            if c < 0:
                left.append(arr[x])
            if c > 0:
                right.append(arr[x])
        
        quick_sort(left, cmp)
        quick_sort(right, cmp)

        n = len(arr)
        n1 = len(left)
        n2 = len(right)
        arr[:n1] = left
        arr[n1:n-n2] = [pivot] * (n - n1 - n2)
        arr[n-n2:] = right