def merge(gArray, low, mid1, mid2, high, destArray):
    i = low
    j = mid1
    k = mid2
    l = low

    while (i < mid1) and (j < mid2) and (k < high):
        if gArray[i] < gArray[j]:
            if gArray[i] < gArray[k]:
                destArray[l] = gArray[i]
                l += 1
                i += 1
            else:
                destArray[l] = gArray[k]
                l += 1
                k += 1
        else:
            if gArray[j] < gArray[k]:
                destArray[l] = gArray[j]
                l += 1
                j += 1
            else:
                destArray[l] = gArray[k]
                l += 1
                k += 1

    while (i < mid1) and (j < mid2):
        if gArray[i] < gArray[j]:
            destArray[l] = gArray[i]
            l += 1
            i += 1
        else:
            destArray[l] = gArray[j]
            l += 1
            j += 1
    
    while (j < mid2) and (k < high):
        if gArray[j] < gArray[k]:
            destArray[l] = gArray[j]
            l += 1
            j += 1
        else:
            destArray[l] = gArray[k]
            l += 1
            k += 1

    while (i < mid1) and (k < high):
        if gArray[i] < gArray[k]:
            destArray[l] = gArray[i]
            l += 1
            i += 1
        else:
            destArray[l] = gArray[k]
            l += 1
            k += 1

    while i < mid1:
        destArray[l] = gArray[i]
        l += 1
        i += 1

    while j < mid2:
        destArray[l] = gArray[j]
        l += 1
        j += 1

    while k < high:
        destArray[l] = gArray[k]
        l += 1
        k += 1

    print("Array durante a mesclagem:", destArray[low:high])

def mergeSort3WayRec(gArray, low, high, destArray):
    if high - low < 2:
        return

    mid1 = low + ((high - low) // 3)
    mid2 = low + 2 * ((high - low) // 3) + 1

    print("Array antes da ordenação:", destArray[low:high])

    mergeSort3WayRec(destArray, low, mid1, gArray)
    mergeSort3WayRec(destArray, mid1, mid2, gArray)
    mergeSort3WayRec(destArray, mid2, high, gArray)

    merge(destArray, low, mid1, mid2, high, gArray)

def mergeSort3Way(gArray, n):
    if n == 0:
        return []

    fArray = gArray.copy()
    mergeSort3WayRec(fArray, 0, n, gArray)
    return fArray


data = [25, 19, 0, -13, 86, 50]
print("Array original:", data)
data = mergeSort3Way(data, len(data))
print("Depois do 3-way merge sort:", data)
