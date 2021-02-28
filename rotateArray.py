def rotateArray(A,k):
    if k == 0 or k == len(A):
        return print(A)
    elif k > len(A):
        return print(A)
    else:
        output = []
        output = A[-k:]
        output.extend(A[0:-k])
        return print(output)

rotateArray([1,2,3,4,5,6,7,8,9,10],2)
rotateArray([1,2,3,4,5,6,7,8,9,10],0)
rotateArray([1,2,3,4,5,6,7,8,9,10],10)
rotateArray([1,2,3,4,5,6,7,8,9,10],11)
rotateArray([1,2,3,4,5,6,7,8,9,10],9)
