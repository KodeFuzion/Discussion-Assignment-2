# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")
# must be in-place sort
def merge_sort(arr,cmp):
    if len(arr) > 1:
        mid = len((arr)) // 2       # Finding the mid of the array
        left = arr[:mid]            # create 2 sub arrays
        right = arr[mid:]
        merge_sort(left, cmp)
        merge_sort(right, cmp)

        # merge 2 arrays
        n1 = len(left)
        n2 = len(right)
        x = 0
        y = 0
        z = 0
        while x < n1 and y < n2:
            if cmp(left[x], right[y]) < 0:
                arr[y] = left[x]
                x = x + 1
            else:
                arr[z] = right[y]
                y = y + 1
                z = z + 1

        while y < n2:
            arr[z] = right[y]
            y = y + 1
            z = z + 1

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

def cmp(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1
