def merge(A, B):
    """merge two sorted lists"""
    result = []

    while A and B:
        if A[0] <= B[0]:
            result.append(A[0])
            del A[0]
        else:
            result.append(B[0])
            del B[0]

    while A:
        result.append(A[0])
        del A[0]
    while B:
        result.append(B[0])
        del B[0]

    return(result)


# merge_sort, main function
def merge_sort(A):
    if len(A) <= 1:
        return(A)

    even, odd = [], []
    for i in range(len(A)):
        if i % 2 == 0:
            even += [A[i]]
        else:
            odd += [A[i]]

    even = merge_sort(even)
    odd = merge_sort(odd)

    return(merge(even, odd))
