def binary_search(A, x):
    A.sort()
    lo = 0
    hi = len(A) - 1
    while hi >= lo:
        guess = (lo + hi) // 2

        if A[guess] == x:
            return(guess)
        elif A[guess] > x:
            hi = guess - 1
        else:
            lo = guess + 1
