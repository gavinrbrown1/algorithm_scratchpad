

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0:
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
            else:
                break
            j -= 1
    return(A)


bases = [
[],
[1],
[9,8,7,6,5,4,3,2,1],
[5,1,7,2,2,3,100]
]

for base in bases:
    print(insertion_sort(base))
