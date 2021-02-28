def evenRemove(B):
    ''' Obtaining list of even keys'''
    outEven = []

    # Apeending even values to a list
    for num in B:
        if num %2 == 0:
            outEven.append(num)
    
    return outEven

def oddOccurranceArray(A):
    ''' Obtaining lowest Odd Occurent value from array '''

    # Creation of dictionary for a sorted array
    counter = dict( (i,A.count(i)) for i in sorted(A))

    # Identifying even keys
    even = evenRemove(list(counter.keys()))
    
    # Removing even keys from dictionary
    [counter.pop(key) for key in even]  

    # Getting lowest occurance from dictionary
    output = min(counter ,key =counter.get)

    return output

print(oddOccurranceArray([1,1,2,3,4,5,6,6,7,7,8,8,9,9,9,9,10]))
print(oddOccurranceArray([1,1,9,9,7]))